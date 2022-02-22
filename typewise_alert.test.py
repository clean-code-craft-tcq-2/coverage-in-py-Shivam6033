import unittest
from concrete_class.hi_active_cooling import HighActiveCooling
from concrete_class.med_active_cooling import MedActiveCooling
from concrete_class.passive_cooling import PassiveCooling


class TypewiseTest(unittest.TestCase):
    def test_classify_temperature_breach_hi_active_cooling_too_low(self):
        for temp_value in range(-100, 0):
            result = HighActiveCooling.classify_temperature_breach(temp_value)
            assert result == 'TOO_LOW'

    def test_classify_temperature_breach_hi_active_cooling_too_high(self):
        for temp_value in range(46, 146):
            result = HighActiveCooling.classify_temperature_breach(temp_value)
            assert result == 'TOO_HIGH'

    def test_classify_temperature_breach_hi_active_cooling_normal(self):
        for temp_value in range(0, 46):
            result = HighActiveCooling.classify_temperature_breach(temp_value)
            assert result == 'NORMAL'

    def test_classify_temperature_breach_med_cooling_too_low(self):
        for temp_value in range(-100, 0):
            result = MedActiveCooling.classify_temperature_breach(temp_value)
            assert result == 'TOO_LOW'

    def test_classify_temperature_breach_med_cooling_too_high(self):
        for temp_value in range(41, 141):
            result = MedActiveCooling.classify_temperature_breach(temp_value)
            assert result == 'TOO_HIGH'

    def test_classify_temperature_breach_med_cooling_normal(self):
        for temp_value in range(0, 41):
            result = MedActiveCooling.classify_temperature_breach(temp_value)
            assert result == 'NORMAL'

    def test_classify_temperature_breach_passive_cooling_too_low(self):
        for temp_value in range(-100, 0):
            result = PassiveCooling.classify_temperature_breach(temp_value)
            assert result == 'TOO_LOW'

    def test_classify_temperature_breach_passive_cooling_too_high(self):
        for temp_value in range(36, 146):
            result = PassiveCooling.classify_temperature_breach(temp_value)
            assert result == 'TOO_HIGH'

    def test_classify_temperature_breach_passive_cooling_normal(self):
        for temp_value in range(0, 36):
            result = PassiveCooling.classify_temperature_breach(temp_value)
            assert result == 'NORMAL'


if __name__ == '__main__':
    unittest.main()
