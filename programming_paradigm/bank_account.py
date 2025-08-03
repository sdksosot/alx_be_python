class BankAccount():
    def __init__(self,account_balance =0):
        self.account_balance =account_balance
    def deposit(self,amount):
        self.account_balance += amount
    def withdraw(self,amount):
        if amount > self.account_balance:
            print("print you cant withdraw that")
        else:
            self.account_balance -= amount
    def show(self):
        print(f'you account balance is {self.account_balance}')

