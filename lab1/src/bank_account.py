class BankAccount:

    def __init__(self, money):
        if not isinstance(money, float):
            raise TypeError

        self.money = money

    def get_balance(self):
        return self.money

    def deposit(self,a):
        self.money = self.money+a

    def withdraw(self,a):
        if a > self.get_balance():
            raise ValueError

        self.money = self.money-a