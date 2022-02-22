
import unittest
from concrete_class.hi_active_cooling import HighActiveCooling
from concrete_class.med_active_cooling import MedActiveCooling
from concrete_class.passive_cooling import PassiveCooling


class TypewiseTest(unittest.TestCase):
    def test_classify_temperature_breach_hi_active_cooling(self):
        for temp_value in range(-100, 100):
            result = HighActiveCooling.classify_temperature_breach(temp_value)
            if temp_value < HighActiveCooling.lowerLimit:
                expected_result = 'TOO_LOW'
            elif temp_value > HighActiveCooling.upperLimit:
                expected_result = 'TOO_HIGH'
            else:
                expected_result = 'NORMAL'
            assert result == expected_result

    def test_classify_temperature_breach_med_active_cooling(self):
        for temp_value in range(-100, 100):
            result = MedActiveCooling.classify_temperature_breach(temp_value)
            if temp_value < MedActiveCooling.lowerLimit:
                expected_result = 'TOO_LOW'
            elif temp_value > MedActiveCooling.upperLimit:
                expected_result = 'TOO_HIGH'
            else:
                expected_result = 'NORMAL'
            assert result == expected_result

    def test_classify_temperature_breach_passive_cooling(self):
        for temp_value in range(-100, 100):
            result = PassiveCooling.classify_temperature_breach(temp_value)
            if temp_value < PassiveCooling.lowerLimit:
                expected_result = 'TOO_LOW'
            elif temp_value > PassiveCooling.upperLimit:
                expected_result = 'TOO_HIGH'
            else:
                expected_result = 'NORMAL'
            assert result == expected_result


if __name__ == '__main__':
    unittest.main()
