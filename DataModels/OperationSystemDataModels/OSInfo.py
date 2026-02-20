
from dataclasses import dataclass

@dataclass
class OSVersion:
    kernel: str
    nodename: str
    machine_hardware_name: str
    os: str

    @classmethod
    def from_line(cls, line: str) -> 'OSVersion':
        parts = line.split()
        if len(parts) != 4:
            raise ValueError(f"Incorrect string format: {line}")
        kernel, nodename, machine_hardware_name, os = parts
        return cls(kernel, nodename, machine_hardware_name, os)