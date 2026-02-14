
from dataclasses import dataclass
from typing import List

from DataModels.NetworkDataModels.PingResultModel import PingResult
from DataModels.NetworkDataModels.TelnetResultModel import TelnetResult


@dataclass
class HostAvailabilityDataModel:
    host: str
    ping: PingResult
    telnet: List[TelnetResult]