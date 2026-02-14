
from dataclasses import dataclass
from typing import List

@dataclass
class Host:
    name: str
    host: str
    ports: List[int]
    ssh: int
