import unittest
from lab1.src.shoppingCart import ShoppingCart

class TestEmail(unittest.TestCase):

    def setUp(self):
        self.empty_card = ShoppingCart([])
        self.card = ShoppingCart(["Apple", "Milk"])

    def test_add_positive(self):
        self.empty_card.add_item("Bread")
        s1 = ShoppingCart(["Bread"])
        self.assertEqual(self.empty_card, s1)

    def test_add_negative(self):
        self.empty_card.add_item("Bread")
        s1 = ShoppingCart(["Ham"])
        self.assertNotEqual(self.empty_card, s1)

    def test_remove_negative(self):
        self.card.remove_item(1)
        self.assertNotEqual(self.empty_card, self.card)

    def test_remove_positive(self):
        self.card.remove_item(1)
        s1 = ShoppingCart(["Apple"])
        self.assertEqual(s1, self.card)

    def test_total(self):
        self.assertEqual(self.card.get_total(),4)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
