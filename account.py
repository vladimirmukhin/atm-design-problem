from csv import DictReader

class Account:
    def __init__(self, id, pin, balance):
        self.id = id
        self.pin = pin
        self.balance = balance

class AccountList:
    def __init__(self):
        self.accounts = {}

        f = open('data/accounts.csv')
        csv = DictReader(f)
        for record in csv:
            self.accounts[record["ACCOUNT_ID"]] = {"PIN": record["PIN"], "BALANCE": record["BALANCE"]}