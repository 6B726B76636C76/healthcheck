
from dataclasses import dataclass

@dataclass
class MemoryInfo:
    total: str
    used: str
    free: str
    shared: str
    buff_cache: str
    available: str

@dataclass
class SwapInfo:
    total: str
    used: str
    free: str

@dataclass
class SystemMemory:
    mem: MemoryInfo
    swap: SwapInfo

    @classmethod
    def from_free_output(cls, output: str) -> 'SystemMemory':
        lines = output.strip().splitlines()
        mem_line = lines[1].split()
        swap_line = lines[2].split()
        mem = MemoryInfo(*mem_line[1:7])
        swap = SwapInfo(*swap_line[1:4])
        return cls(mem, swap)
