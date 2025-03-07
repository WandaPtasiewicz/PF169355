
class ShoppingCart:
    cart = []


    def add_item(self,item):
        self.cart.append(item)

    def remove_item(self,item):
        self.cart.remove(item)

    def get_total(self,):
        return len(self.cart)

    def clear(self):
        self.cart.clear()