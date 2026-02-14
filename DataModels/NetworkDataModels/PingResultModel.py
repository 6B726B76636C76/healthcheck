
from dataclasses import dataclass

@dataclass
class PingResult:
    host: str
    average_time: float
    loss: float
    successful: bool