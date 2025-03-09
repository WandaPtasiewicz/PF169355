import unittest
from unittest import TestCase

from lab1.src.is_palindrome import is_palindrome

class TestIsPalindrome(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_is_polindrome_positive(self):
        self.assertTrue(is_palindrome("kajak"))

    def test_is_polindrome_negative(self):
        self.assertFalse(is_palindrome("kajbbak"))

    def test_is_polindrome_big_letter_positive(self):
        self.assertTrue(is_palindrome("Kajak"))

    def test_is_polindrome_not_alfa_number_positive(self):
        self.assertTrue(is_palindrome("Kaj@ak"))



if __name__ =="__main__":
    unittest.main()