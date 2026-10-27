'''Write a class BankAccount with balance
and deposit(), and a class SavingsAccount(BankAccount)
with apply_interest(rate).
Input Format
First line: initial balance.
Second line: deposit.
Third line: interest rate.'''
class BankAccount:
    def __init__(self,balance):
        self.balance = balance
    def deposit(self):
        d = float(input("Enter Amount: "))
        self.balance += d
class SavingsAccount(BankAccount):
    def apply_interest(self, rate):
        self.balance += self.balance*rate/100

sa = SavingsAccount(float(input("Enter balance : ")))
sa.deposit()
sa.apply_interest(float(input("Rate of Intrest : ")))
print(sa.balance)

