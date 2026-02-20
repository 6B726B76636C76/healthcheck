
from dataclasses import dataclass
from DataModels.NetworkDataModels.HostAvailabilityModel import HostAvailabilityDataModel
from DataModels.OperationSystemDataModels import CPUInfo, RAMInfo, HDDInfo, ActiveUsersInfo, UptimeInfo, OSInfo

@dataclass
class ServerMetricsData:
    cpu: CPUInfo.CpuLoadInfo
    ram: RAMInfo.SystemMemory
    hdd: HDDInfo.HDDInfo
    active_users: ActiveUsersInfo.ActiveUsers
    uptime: UptimeInfo.UptimeData
    os_info: OSInfo.OSVersion

@dataclass
class HealthCheckHostInfo:
    ports: HostAvailabilityDataModel
    metrics_data: ServerMetricsData

