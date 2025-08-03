import sys
from bank_account import BankAccount

def main():
    if len(sys.argv) < 2:
        print("Usage: python main-0.py [command] [amount]")
        print("Commands: create, deposit, withdraw, balance")
        return
    
    # Initialize account (in real app, you'd persist this)
    account = BankAccount(100)  # Starting with $100 for demo
    
    command = sys.argv[1].lower()
    
    if command == "create":
        print("Account created with $0.00 balance")
    elif command == "deposit":
        if len(sys.argv) < 3:
            print("Please specify amount to deposit")
            return
        amount = float(sys.argv[2])
        if account.deposit(amount):
            print(f"Deposited ${amount:.2f}")
        else:
            print("Invalid deposit amount")
    elif command == "withdraw":
        if len(sys.argv) < 3:
            print("Please specify amount to withdraw")
            return
        amount = float(sys.argv[2])
        if account.withdraw(amount):
            print(f"Withdrew ${amount:.2f}")
        else:
            print("Insufficient funds or invalid amount")
    elif command == "balance":
        account.display_balance()
    else:
        print("Invalid command")

if __name__ == "__main__":
    main()

