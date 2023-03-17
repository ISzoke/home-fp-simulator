from abc import ABC, abstractmethod
import datetime
from typing import List

class EnergyProducer(ABC):

    @abstractmethod
    def getProduction(self, from_time: datetime, to_time: datetime, consumption: List[float]) -> List[float]:
        pass

    @abstractmethod
    def getProduction(self, from_time: datetime, length_seconds: float, consumption: List[float]) -> List[float]:
        pass
