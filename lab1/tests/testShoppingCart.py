import unittest
from lab1.src.shoppingCart import ShoppingCart

class TestEmail(unittest.TestCase):

    def setUp(self):
        self.cart = ShoppingCart("Apple","Milk")
        self.empty_cart = ShoppingCart()

    def tearDown(self):
        pass