
from dataclasses import dataclass
from typing import List

from DataModels.NetworkDataModels.PingResultModel import PingResult
from DataModels.NetworkDataModels.TelnetResultModel import TelnetResult


@dataclass
class HostAvailabilityData:
    ping: PingResult
    tenlet: List[TelnetResult]