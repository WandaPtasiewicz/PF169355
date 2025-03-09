
class ShoppingCart:

    def __init__(self, items):
        if not isinstance(items, list):
            raise TypeError

        for elem in items:
            if not isinstance(elem, str):
                raise ValueError

        self.items = items

    def __str__(self):
        return f"Shopping card: {self.items}."


    def add_item(self,item):
        if not isinstance(item, str):
            raise ValueError
        self.items.append(item)

    def remove_item(self,index):
        if not isinstance(index, int):
            raise TypeError

        if 0 > index or index >= len(self.items):
            raise IndexError

        self.items.remove(self.items[index])

    def get_total(self):
        return len(self.items)*2

    def clear(self):
        self.items.clear()

    def __eq__(self, other):
        return self.items == other.items