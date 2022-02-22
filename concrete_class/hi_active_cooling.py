from abstract_class.cooling_service import CoolingService


class HighActiveCooling(CoolingService):
    lowerLimit = 0
    upperLimit = 45

    @classmethod
    def classify_temperature_breach(cls, value):
        if value < cls.lowerLimit:
            return 'TOO_LOW'
        if value > cls.upperLimit:
            return 'TOO_HIGH'
        return 'NORMAL'
