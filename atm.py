class Atm:
    def __init__(self):
        self.cash = 10000

    def dispense(self, amount):
        if self.cash - amount < 0:
            print("Unable to dispense full amount requested at this time.")
            amount = self.cash
        self.cash-=amount

        return amount

    def accept(self, amount):
        self.cash+=amount