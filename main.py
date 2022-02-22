from Enums.breach_type import InferBreachType
from Enums.cooling_type import CoolingType
from concrete_class.battery import Battery

battery = Battery(45, CoolingType.MED_ACTIVE, InferBreachType.EMAIL)
battery.check_and_alert()
