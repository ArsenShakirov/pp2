class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}, New Balance: {self.balance}")
        else:
            print("Insufficient funds for withdrawal")

# Example usage
account = Account("John", 100)
account.deposit(50)
account.withdraw(30)
account.withdraw(150)
