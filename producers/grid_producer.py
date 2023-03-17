import datetime
from typing import List

from producers.producer_abc import EnergyProducer

class GridProducer(EnergyProducer):

    def __init__(self) -> None:
        super().__init__()
    
    def getProduction(self, from_time: datetime, to_time: datetime, consumption: List[float]) -> List[float]:
        return consumption

    def getProduction(self, from_time: datetime, length_seconds: float, consumption: List[float]) -> List[float]:
        return consumption