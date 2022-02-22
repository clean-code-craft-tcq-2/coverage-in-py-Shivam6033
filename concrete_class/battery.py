from Enums.breach_type import InferBreachType
from Enums.cooling_type import CoolingType


class Battery:
    def __init__(self, temperature_value: int, cooling_type: CoolingType, alert_target: InferBreachType):
        self.temperature_value = temperature_value
        self.cooling_type = cooling_type.value
        self.alert_target = alert_target

    def check_and_alert(self):
        breach_type = self.cooling_type.classify_temperature_breach(self.temperature_value)
        self.alert_target.value.send_message(breach_type)
