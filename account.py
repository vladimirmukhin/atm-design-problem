from csv import DictReader

class Account:
    def __init__(self, id, pin, balance):
        self.id = id
        self.pin = pin
        self.balance = float(balance)

    def withdraw(self, amount):
        if self.balance > 0:
            overdraft = ""
            if self.balance - amount < 0:
                overdraft = "You have been charged an overdraft fee of $5. "
                self.balance-=5
            self.balance-=amount

            print(f"Amount dispensed: ${amount}")
            print(f"{overdraft}Current balance: {self.balance}")

            return True
        else:
            print("Your account is overdrawn! You may not make withdrawals at this time.")
            return False

    def deposit(self,amount):
        self.balance+=amount


class AccountList:
    def __init__(self):
        self.accounts = {}

        f = open('data/accounts.csv')
        csv = DictReader(f)
        for record in csv:
            self.accounts[record["ACCOUNT_ID"]] = Account(record["ACCOUNT_ID"],record["PIN"],record["BALANCE"])