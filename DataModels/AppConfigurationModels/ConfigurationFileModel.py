
from dataclasses import dataclass
from typing import List

@dataclass
class Host:
    name: str
    host: str
    ports: List[int]
    ssh_port: int
    username: str
    ssh_key: str
    ssh_key_passphrase: str
    checkout_interval: str
