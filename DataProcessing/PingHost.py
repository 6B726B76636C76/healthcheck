from icmplib import async_ping
from DataModels.NetworkDataModels.PingResultModel import PingResult

async def ping_host(host: str) -> PingResult|None:
    try:
        ping_result = await async_ping(host, count=5, timeout=2, privileged=False)
        return PingResult(
            host=host,
            average_time=f"{ping_result.avg_rtt if ping_result.is_alive else 0.0} ms",
            loss=int(ping_result.packet_loss * 100),
            successful=ping_result.is_alive
        )
    except Exception as e:
        print(f"Error! {e}")
        #TODO ALERT
        return None