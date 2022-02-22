from abstract_class.cooling_service import CoolingService


class MedActiveCooling(CoolingService):
    lowerLimit = 0
    upperLimit = 40

    @classmethod
    def classify_temperature_breach(cls, value):
        if value < cls.lowerLimit:
            return 'TOO_LOW'
        if value > cls.upperLimit:
            return 'TOO_HIGH'
        return 'NORMAL'
