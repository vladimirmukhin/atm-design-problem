from csv import DictReader
from logger import Logger
from os import listdir

class Account:
    def __init__(self, id, pin, balance):
        self.id = id
        self.pin = pin
        self.balance = float(balance)
        self.logger = Logger()

    def withdraw(self, amount):
        if self.balance > 0:
            overdraft = ""
            if self.balance - amount < 0:
                overdraft = "You have been charged an overdraft fee of $5. "
                self.balance-=5
            self.balance-=amount

            print(f"Amount dispensed: ${amount}")
            print(f"{overdraft}Current balance: {self.balance}")

            self.logger.log_transaction(self.id,-amount,self.balance)

            return True
        else:
            print("Your account is overdrawn! You may not make withdrawals at this time.")
            return False

    def deposit(self,amount):
        self.balance+=amount

        self.logger.log_transaction(self.id,amount,self.balance)


class AccountList:
    def __init__(self):
        self.accounts = {}
        existing_accounts = listdir('data/account_history')

        f = open('data/accounts.csv')
        csv = DictReader(f)
        for record in csv:
            if record["ACCOUNT_ID"] in existing_accounts:
                f = open(f"data/account_history/{record['ACCOUNT_ID']}")
                last_line = f.readlines()[-1]
                balance = last_line.split(' ')[3]
            else:
                balance = record["BALANCE"]

            self.accounts[record["ACCOUNT_ID"]] = Account(record["ACCOUNT_ID"],record["PIN"],balance)