import asyncio
import telnetlib3
from typing import List
from DataModels.NetworkDataModels.TelnetResultModel import TelnetResult

async def telnet_ports(host: str, ports: List[int]) -> List[TelnetResult]:
    results: List[TelnetResult] = []
    for port in ports:
        try:
            reader, writer = await asyncio.wait_for(
                telnetlib3.open_connection(host, port),
                timeout=3
            )
            writer.close()
            results.append(TelnetResult(port=port, successful=True))
        except (asyncio.TimeoutError, ConnectionRefusedError, OSError) as e:
            results.append(TelnetResult(port=port, successful=False))
        except Exception as e:
            print(f"Unexpected port error! {host}:{port} {e}")
            results.append(TelnetResult(port=port, successful=False))
    return results