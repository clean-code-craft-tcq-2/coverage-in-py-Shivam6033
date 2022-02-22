from abc import ABC, abstractmethod


class AlertService(ABC):
    breach_type = None

    @classmethod
    @abstractmethod
    def send_message(cls, breachType):
        pass
