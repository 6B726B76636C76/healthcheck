import asyncio
import socket
import paramiko
from typing import List
from DataProcessing.PingHost import ping_host
from DataProcessing.TelnetPortHost import telnet_ports
from paramiko import AuthenticationException, SSHClient, SSHException
from DataModels.AppConfigurationModels.ConfigurationFileModel import Host
from DataModels.HostData import HealthCheckHostInfo, ServerMetricsData
from DataModels.NetworkDataModels.HostAvailabilityModel import HostAvailabilityDataModel
from DataProcessing.ConfigReader.ConfigurationFileReader import config_reader
from DataProcessing.OperationSystem.GetOsInfo import get_active_users, get_cpu_load, get_os_info, get_partition_info, get_ram_info, get_uptime_info


async def collect_availability_data(host: Host)-> HostAvailabilityDataModel:
        try:
            ping_result = await ping_host(host.host)
            telnet_result = await telnet_ports(host.host, host.ports)
            return HostAvailabilityDataModel(
                host=host.host,
                ping=ping_result,
                telnet=telnet_result
            )
        except Exception as e:
            print(f"{e}")
            #TODO LOGGER
            exit(1)

async def collect_metrics_data(client: SSHClient, host: Host) -> ServerMetricsData | None:
    if not host.ssh_key or not host.ssh_port:
        return None
    try:
        await asyncio.to_thread(
            client.connect,
            hostname=host.host,
            port=host.ssh_port,
            username=host.username,
            key_filename=host.ssh_key
        )
        cpu = await asyncio.to_thread(get_cpu_load, client)
        ram = await asyncio.to_thread(get_ram_info, client)
        hdd = await asyncio.to_thread(get_partition_info, client)
        active_users = await asyncio.to_thread(get_active_users, client)
        uptime = await asyncio.to_thread(get_uptime_info, client)
        os_info = await asyncio.to_thread(get_os_info, client)

        return ServerMetricsData(
            cpu=cpu,
            ram=ram,
            hdd=hdd,
            active_users=active_users,
            uptime=uptime,
            os_info=os_info
        )
    except (AuthenticationException, SSHException, socket.error, FileNotFoundError) as e:
        print(f"Error! с {host.host}: {e}")
        return None
    finally:
        await asyncio.to_thread(client.close)
