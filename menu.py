from cmd import Cmd
from account import AccountList
from atm import Atm
from os import listdir

class MyPrompt(Cmd):
    def preloop(self):
        self.account_list = AccountList().accounts
        self.account_id = None
        self.atm = Atm()


    def do_auth(self, arg):
        '''Authenticates an account locally until they are logged out.'''

        arg = arg.split()

        if len(arg) != 2:
            print(f"auth requires exactly 2 arguments, {len(arg)} were given")
            return

        try:
            int(arg[0])
            int(arg[1])
            account_id = arg[0]
            pin = arg[1]
        except ValueError:
            print(f"auth requires numeric arguments")
            return

        if account_id not in self.account_list:
            print("Authentication faileda.")
            return

        if pin != self.account_list[account_id].pin:
            print("Authentication failedb.")
            return

        print(f"{account_id} successfully authenticated")
        self.account_id = account_id
        return


    def do_withdraw(self, arg):
        '''Removes value from the authorized account.'''

        if not self.account_id:
            print("Authentication required")

        arg = arg.split()

        if len(arg) != 1:
            print(f"withdraw requires exactly 1 argument, {len(arg)} were given")
            return

        try:
            value = int(arg[0])
        except ValueError:
            print(f"withdraw requires numeric arguments")
            return

        if int(value) % 20 != 0:
            print("Withdrawal amount must be a multiple of 20.")
            return

        if self.account_list[self.account_id].withdraw(int(value)):
            self.atm.dispense(int(value))


    def do_deposit(self, arg):
        '''Adds value to the authorized account.'''

        if not self.account_id:
            print("Authentication required")
            return

        arg = arg.split()

        if len(arg) != 1:
            print(f"deposit requires exactly 1 argument, {len(arg)} were given")
            return

        try:
            value = int(arg[0])
        except ValueError:
            print(f"withdraw requires numeric arguments")
            return

        self.atm.accept(int(value))
        self.account_list[self.account_id].deposit(int(value))


    def do_balance(self, arg):
        '''Returns the account’s current balance.'''

        if not self.account_id:
            print("Authentication required")
            return

        print(self.account_list[self.account_id].balance)


    def do_history(self, arg):
        '''Returns the account’s transaction history.'''

        if not self.account_id:
            print("Authentication required")
            return

        existing_accounts = listdir('data/account_history')
        if self.account_id in existing_accounts:
            history = open(f"data/account_history/{self.account_id}").readlines()
            for i in range(len(history)-1,-1,-1):
                print(history[i][:-1])
        else:
            print("No history found")

    def do_logout(self, arg):
        '''Deactivates the currently authenticated account.'''

        self.account_id = None


    def do_end(self, arg):
        '''Shuts down the server.'''
        return True
