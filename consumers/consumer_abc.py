from abc import ABC, abstractmethod
import datetime
from typing import List

class EnergyConsumer(ABC):

    @abstractmethod
    def getConsumption(self, from_time: datetime, to_time: datetime) -> List[float]:
        pass

    @abstractmethod
    def getConsumption(self, from_time: datetime, length_seconds: float) -> List[float]:
        pass


    