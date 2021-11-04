from cmd import Cmd
from account import AccountList
from atm import Atm

class MyPrompt(Cmd):
    def preloop(self):
        self.account_list = AccountList().accounts
        self.account_id = None
        self.atm = Atm()

    def do_auth(self, arg):
        '''Authenticates an account locally until they are logged out.'''

        arg = arg.split()

        if len(arg) != 2:
            print("Authentication failed.")
            return

        if arg[0] not in self.account_list:
            print("Authentication failed.")
            return

        if arg[1] != self.account_list[arg[0]].pin:
            print("Authentication failed.")
            return

        print(f"{arg[0]} successfully authenticated")
        self.account_id = arg[0]
        return


    def do_withdraw(self, arg):
        '''Removes value from the authorized account.'''

        if not self.account_id:
            print("Authentication required")

        if int(arg) % 20 != 0:
            print("Withdrawal amount must be a multiple of 20.")
            return

        if self.account_list[self.account_id].withdraw(int(arg)):
            self.atm.dispense(int(arg))


    def do_deposit(self, arg):
        '''Adds value to the authorized account.'''

        if not self.account_id:
            print("Authentication required")

        self.atm.accept(int(arg))

        self.account_list[self.account_id].deposit(int(arg))


    def do_balance(self, subcommand):
        '''Returns the account’s current balance.'''

        if not self.account_id:
            print("Authentication required")
            return

        print(self.account_list[self.account_id].balance)


    def do_history(self, subcommand):
        '''Returns the account’s transaction history.'''

        if not self.account_id:
            print("Authentication required")


    def do_logout(self, subcommand):
        '''Deactivates the currently authenticated account.'''

        self.account_id = None


    def do_end(self, subcommand):
        '''Shuts down the server.'''
        return True