import unittest
from lab1.src.validate_email import validate_email


class TestEmail(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    def test_validate_positive(self):
        self.assertTrue(validate_email("info@gmail.com"))

    def test_validate_negative(self):
        self.assertFalse(validate_email("infogmail.com"))

    def test_type_error(self):
        with self.assertRaises(TypeError):
            validate_email(444)



if __name__ =="__main__":
    unittest.main()