import datetime
from typing import List

from consumers.consumer_abc import EnergyConsumer

class HomeAssistantET340Consumer(EnergyConsumer):

    def __init__(self) -> None:
        super().__init__()
    
    def getConsumption(self, from_time: datetime, to_time: datetime) -> List[float]:
        return [1.1, 1.2, 1.3]

    
    def getConsumption(self, from_time: datetime, length_seconds: float) -> List[float]:
        return [1.1, 1.2, 1.3]
