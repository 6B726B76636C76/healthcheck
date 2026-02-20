from dataclasses import dataclass
from datetime import datetime
import re
from typing import List

@dataclass
class ActiveUser:
    username: str
    terminal: str
    login_time: str
    ip: str

    @classmethod
    def from_line(cls, line: str) -> 'ActiveUser':
        line = line.strip()
        if not line:
            raise ValueError("Empty string")
        ip_match = re.search(r'\(([^)]+)\)$', line)
        ip = ip_match.group(1) if ip_match else ''
        line_without_ip = re.sub(r'\s*\([^)]+\)$', '', line)
        parts = line_without_ip.split()
        if len(parts) < 4:
            raise ValueError(f"Incorrect string format: {line}")

        username = parts[0]
        terminal = parts[1]
        date_str = parts[2]
        time_str = parts[3]

        dt_str = f"{date_str} {time_str}"
        try:
            login_time = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
        except ValueError as e:
            raise ValueError(f"Date parsing error: {dt_str}") from e

        return cls(username, terminal, login_time, ip)
@dataclass
class ActiveUsers:
    users: List[ActiveUser]