import unittest
from lab1.src.temperature_converter import TemperatureConverter

class TestTemperatureConverter(unittest.TestCase):

    def setUp(self):
        self.temperature_converter = TemperatureConverter()

    def tearDown(self):
        pass

    def test_celsius_to_fahrenheit_positive(self):
        self.assertEqual(self.temperature_converter.celsius_to_fahrenheit(2),36)

    def test_celsius_to_fahrenheit_negative(self):
        self.assertNotEqual(self.temperature_converter.celsius_to_fahrenheit(2),35)

    def test_fahrenheit_to_celsius_positive(self):
        self.assertEqual(self.temperature_converter.fahrenheit_to_celsius(50),9)

    def test_fahrenheit_to_celsius_negative(self):
        self.assertNotEqual(self.temperature_converter.fahrenheit_to_celsius(50),0)

    def test_celsius_to_kelvin_positive(self):
        self.assertEqual(self.temperature_converter.celsius_to_kelvin(0),273.15)

    def test_celsius_to_kelvin_negative(self):
        self.assertNotEqual(self.temperature_converter.celsius_to_kelvin(580),223.15)

    def test_kelvin_to_celsius_positive(self):
        self.assertEqual(self.temperature_converter.kelvin_to_celsius(273.15),0)

    def test_kelvin_to_celsius_negative(self):
        self.assertNotEqual(self.temperature_converter.kelvin_to_celsius(50),23.15)

if __name__ =="__main__":
    unittest.main()