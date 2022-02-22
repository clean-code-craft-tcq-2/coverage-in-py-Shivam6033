from abc import ABC, abstractmethod


class CoolingService(ABC):
    lowerLimit = 0
    upperLimit = 0

    @classmethod
    @abstractmethod
    def classify_temperature_breach(cls, value):
        pass
