
from dataclasses import dataclass
from typing import List


@dataclass
class PartitionInfo:
    fs: str
    size: str
    used: str
    available: str
    use_percent: str
    mounted_on: str

    @classmethod
    def from_line(cls, line: str) -> 'PartitionInfo':
        parts = line.strip().split()
        if len(parts) != 6:
            raise ValueError(f"Expected 6 columns, got {len(parts)}: {line}")
        fs, size, used, available, use_percent, mounted_on = parts
        return cls(fs, size, used, available, use_percent, mounted_on)

@dataclass
class PartitionInodes:
    fs: str
    inodes: str
    used: str
    available: str
    use_percent: str
    mounted_on: str

    @classmethod
    def from_line(cls, line: str) -> 'PartitionInodes':
        parts = line.strip().split()
        if len(parts) != 6:
            raise ValueError(f"Expected 6 columns, got {len(parts)}: {line}")
        fs, inodes, used, available, use_percent, mounted_on = parts
        return cls(fs, inodes, used, available, use_percent, mounted_on)

@dataclass
class HDDInfo:
    partitions: List[PartitionInfo]
    partition_inodes: List[PartitionInodes]