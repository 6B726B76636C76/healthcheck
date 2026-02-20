from typing import List
from paramiko import SSHClient
from DataModels.OperationSystemDataModels import HDDInfo
from DataModels.OperationSystemDataModels.RAMInfo import SystemMemory
from DataModels.OperationSystemDataModels.UptimeInfo import UptimeData
from DataModels.OperationSystemDataModels.OSInfo import OSVersion
from DataModels.OperationSystemDataModels.ActiveUsersInfo import ActiveUser, ActiveUsers
from DataModels.OperationSystemDataModels.CPUInfo import CpuLoadInfo
from DataModels.OperationSystemDataModels.HDDInfo import PartitionInfo, PartitionInodes

def _execute_command(client: SSHClient, command: str) -> str:
    stdin, stdout, stderr = client.exec_command(command)
    exit_status = stdout.channel.recv_exit_status()
    out = stdout.read().decode()
    err = stderr.read().decode().strip()
    if exit_status != 0:
        raise RuntimeError(f"Command '{command}' failed with code {exit_status}: {err}")
    return out

def get_active_users(client: SSHClient, get_active_users_command: str = "who") -> List[ActiveUser]:
    records: List[ActiveUser] = []
    output = _execute_command(client, get_active_users_command)
    for line in output.splitlines():
        line = line.strip()
        if line:
            try:
                records.append(ActiveUser.from_line(line))
            except ValueError as e:
                print(f"Missing string: {line} — {e}")
    return ActiveUsers(
        users=records
    )

def get_cpu_load(client: SSHClient, get_cpu_load_command: str ="cat /proc/loadavg") -> CpuLoadInfo:
    output = _execute_command(client, get_cpu_load_command)
    return CpuLoadInfo.from_line(output)

def get_partition_info(client: SSHClient, get_partitions_info_command: str = "df -h / /boot", get_inode_info_command: str = "df -i") -> HDDInfo:
    partitions: List[PartitionInfo] = []
    inodes: List[PartitionInodes] = []

    hdd_output = _execute_command(client, get_partitions_info_command)
    inode_output = _execute_command(client, get_inode_info_command)
    hdd_lines = hdd_output.splitlines()
    inode_lines = inode_output.splitlines()

    for line in hdd_lines[1:]:
        line = line.strip()
        if not line:
            continue
        try:
            partitions.append(PartitionInfo.from_line(line))
        except ValueError as e:
            #TODO LOGGER
            print(f"Skipping malformed line: {line} — {e}")

    for line in inode_lines[1:]:
        line = line.strip()
        if not line:
            continue
        try:
            inodes.append(PartitionInodes.from_line(line))
        except ValueError as e:
            #TODO LOGGER
            print(f"Skipping malformed line: {line} — {e}")
    
    return HDDInfo.HDDInfo(
        partitions,
        partition_inodes=inodes
    )


def get_inode_info(client: SSHClient, get_inode_info_command: str = "df -i") -> List[PartitionInodes]:
    result: List[PartitionInodes] = []
    output = _execute_command(client, get_inode_info_command)
    for line in output.splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            result.append(PartitionInodes.from_line(line))
        except ValueError as e:
            #TODO LOGGER
            print(f"Skipping malformed line: {line} — {e}")


def get_os_info(client: SSHClient, get_os_info_command: str = "uname -s -n -m -o") -> OSVersion:
    output = _execute_command(client, get_os_info_command)
    return OSVersion.from_line(output)

def get_ram_info(client: SSHClient, get_ram_info_command: str = "free -h"):
    output = _execute_command(client, get_ram_info_command)
    return SystemMemory.from_free_output(output)

def get_uptime_info(client: SSHClient, get_uptime_info_command: str = "uptime -p") -> UptimeData:
    output = _execute_command(client, get_uptime_info_command)
    return UptimeData(output)
