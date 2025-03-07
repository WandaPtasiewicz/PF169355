import unittest
from lab1.src.string_manipulator import StringManipulator



class TestEmail(unittest.TestCase):

    def setUp(self):
        self.string_manipulator = StringManipulator()

    def tearDown(self):
        pass

    def test_reverse_blank_positive(self):
        self.assertEqual(self.string_manipulator.reverse_string(" ")," ")

    def test_reverse_positive(self):
        self.assertEqual(self.string_manipulator.reverse_string("mama"),"amam")

    def test_reverse_negative(self):
        self.assertNotEqual(self.string_manipulator.reverse_string("mama"),"mama")

    def test_capitalize_negative(self):
        self.assertNotEqual(self.string_manipulator.capitalize_words("mama michała"),"mama Michała")

    def test_count_words_positive(self):
        self.assertEqual(self.string_manipulator.count_words("mama michała jezdzi autem "),4)

    def test_count_words_negative(self):
        self.assertNotEqual(self.string_manipulator.count_words("mama michała jezdzi autem "),1)

if __name__ =="__main__":
    unittest.main()