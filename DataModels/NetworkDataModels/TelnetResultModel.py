
from dataclasses import dataclass

@dataclass
class TelnetResult:
    port: int
    successful: bool
