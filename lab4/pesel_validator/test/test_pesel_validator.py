import unittest

from pesel_validator.src.pesel_validator import PeselValidator


class TestPeselValidator(unittest.TestCase):
    def setup(self):
        pass

    def tearDown(self):
        pass

    def test_pesel_format(self):
        self.assertTrue(PeselValidator.validate_format("02322004441"))

    def test_check_digit(self):
        self.assertTrue(PeselValidator.validate_check_digit("02322004441"))

    def test_birth_date(self):
        self.assertTrue(PeselValidator.validate_birth_date("02322004441","2002-12-20"))

    def test_gender(self):
        self.assertEqual(PeselValidator.get_gender("02322004441"),"K")

    def test_is_valid(self):
        self.assertTrue(PeselValidator.is_valid("02322004441","2002-12-20","K"))



if __name__ == "__main__":
    unittest.main()