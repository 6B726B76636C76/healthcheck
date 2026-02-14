import asyncio
from typing import List
from DataModels.NetworkDataModels.HostAvailabilityModel import HostAvailabilityDataModel
from DataProcessing.DataCollector import collect_availability_data

async def main():
    result: List[HostAvailabilityDataModel] = await collect_availability_data("test_config.toml")
    for host in result:
        print(f"host - {host.host}")
        print(f"ping result - {host.ping.successful}")
        print(f"ping average time - {host.ping.average_time}")
        print(f"ping packet loss - {host.ping.loss}%")
        for port in host.telnet:
            print(f"port {port.port} - {port.successful}")
        print("\n")
asyncio.run(main())