import unittest
from lab1.src.fibonacci import fibonacci


class TestEmail(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    def test_fibonacci_nr0(self):
        self.assertEqual(fibonacci(0),0)

    def test_fibonacci_nr10(self):
        self.assertEqual(fibonacci(10),55)

    def test_fibonacci_nr19(self):
        self.assertEqual(fibonacci(19),4181)

    def test_value_error_negative_number(self):
        with self.assertRaises(ValueError):
            fibonacci(-2)

    def test_value_error_string(self):
        with self.assertRaises(ValueError):
            fibonacci("papa")




if __name__ =="__main__":
    unittest.main()