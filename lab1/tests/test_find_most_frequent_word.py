import unittest
from lab1.src.find_most_frequent_word import find_most_frequent_word

class TestEmail(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_function_positive(self):
        self.assertEqual(find_most_frequent_word("Ala ma kota Krzysia i kota Felka"),["kota"])

    def test_function_negative(self):
        self.assertNotEqual(find_most_frequent_word("Ala ma  Krzysia i kota Felka"),["kota"])

    def test_function_positive_two_same(self):
        self.assertEqual(find_most_frequent_word("Ala ma kota Felka i kota Felka"),['kota','felka'])

    def test_function_positive_blank(self):
        self.assertEqual(find_most_frequent_word(""),None)

if __name__ =="__main__":
    unittest.main()