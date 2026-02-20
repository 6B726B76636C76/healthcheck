
from dataclasses import dataclass
from datetime import datetime
from typing import Tuple

@dataclass
class CpuLoadInfo:
    load_1min: str
    load_5min: str
    load_15min: str
    running_total: str
    last_user_pid: str

    @classmethod
    def from_line(cls, line: str) -> 'CpuLoadInfo':
        parts = line.strip().split()
        if len(parts) != 5:
            raise ValueError(f"Incorrect string format: {line}")
        load1, load5, load15 = map(float, parts[:3])

        running_str, total_str = parts[3].split('/')
        running = int(running_str)
        total = int(total_str)
        last_pid = int(parts[4])

        return CpuLoadInfo(
            load_1min=load1,
            load_5min=load5,
            load_15min=load15,
            running_total=f"{running}/{total}",
            last_user_pid=last_pid
        )