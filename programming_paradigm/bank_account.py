class BankAccount:
    """A class representing a simple bank account"""
    
    def __init__(self, initial_balance=0.0):
        """
        Initialize a bank account with an optional starting balance
        
        Args:
            initial_balance (float): Starting balance (default 0.0)
        """
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        """
        Deposit money into the account
        
        Args:
            amount (float): Amount to deposit
            
        Returns:
            bool: True if successful, False if invalid amount
        """
        if amount > 0:
            self.account_balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        """
        Withdraw money from the account
        
        Args:
            amount (float): Amount to withdraw
            
        Returns:
            bool: True if successful, False if insufficient funds or invalid amount
        """
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False
    
    def display_balance(self):
        """Display the current account balance"""
        print(f"Current Balance: ${self.account_balance:.2f}")
