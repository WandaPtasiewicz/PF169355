import unittest
from lab1.src.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_sum_int(self):
        self.assertEqual(self.calculator.add(6,3),9)

    def test_sum_int_negative(self):
        self.assertNotEqual(self.calculator.add(6,3),12)

    def test_sum_int_float(self):
        self.assertAlmostEqual(self.calculator.add(6.1,3.0),9.1)

    def test_subtract_int(self):
        self.assertEqual(self.calculator.subtract(6,3),3)

    def test_subtract_int_negative(self):
        self.assertNotEqual(self.calculator.subtract(6,9),-33)

    def test_multiply_int(self):
        self.assertEqual(self.calculator.multiply(6,0.5),3)

    def test_multiply_int_negative(self):
        self.assertNotEqual(self.calculator.multiply(6,0),6)

    def test_divide_int(self):
        self.assertEqual(self.calculator.divide(6,2),3)

    def test_divide_int_error(self):
        
        with self.assertRaises(ValueError):
            self.calculator.divide(6,0)

    def tearDown(self):
        pass

if __name__ =="__main__":
    unittest.main()