import unittest
from src.pesel_validator import PeselValidator

class TestPeselValidator(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def test_pesel_format(self):
        self.assertTrue(PeselValidator.validate_format("12345678901"))

    def test_check_digit(self):
        self.assertTrue(PeselValidator.validate_check_digit("12345678901"))



if __name__ == "__main__":
    unittest.main()