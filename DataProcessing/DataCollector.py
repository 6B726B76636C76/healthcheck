from typing import List
from DataModels.NetworkDataModels.HostAvailabilityModel import HostAvailabilityDataModel
from DataProcessing.ConfigReader.ConfigurationFileReader import config_reader
from DataProcessing.PingHost import ping_host
from DataProcessing.TelnetPortHost import telnet_ports

async def collect_availability_data(config_path: str)-> List[HostAvailabilityDataModel]:
    config_data = config_reader(config_path)
    if config_data is not None:
        result: List[HostAvailabilityDataModel] = []
        for host in config_data:
            try:
                ping_result = await ping_host(host.host)
                telnet_result = await telnet_ports(host.host, host.ports)
                result.append(HostAvailabilityDataModel(
                    host=host.host,
                    ping=ping_result,
                    telnet=telnet_result
                ))
            except Exception as e:
                print(f"{e}")
        return result
    else:
        print("Incorrect configuration file!")
        #TODO LOGGER
        exit(1)