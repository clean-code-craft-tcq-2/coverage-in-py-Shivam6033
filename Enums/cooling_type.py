from enum import Enum

from concrete_class.hi_active_cooling import HighActiveCooling
from concrete_class.med_active_cooling import MedActiveCooling
from concrete_class.passive_cooling import PassiveCooling


class CoolingType(Enum):
    PASSIVE = PassiveCooling()
    HIGH_ACTIVE = HighActiveCooling()
    MED_ACTIVE = MedActiveCooling()