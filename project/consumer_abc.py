from abc import ABC, abstractmethod

class EnergyConsumer(ABC):

    @abstractmethod
    def getConsumption(self, from_time: , to_time: ):
        pass

    @abstractmethod
    def my_other_method(self, arg1, arg2):
        pass

    # Add more abstract methods as needed