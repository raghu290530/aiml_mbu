'''Write a class BankAccount with balance
and deposit(), and a class
SavingsAccount(BankAccount) with
apply_interest(rate).'''
class BankAccount:
    def __init__(self,b):
        self.balance=b
    def deposit(self):
        d = int(input("Enter Deposit amount : "))
        self.balance += d
class SavingsAccount(BankAccount):
    def apply_interest(self,rate):
        self.balance += self.balance*10/100
sa = SavingsAccount(int(input("Enter Balance : ")))
sa.deposit()
sa.apply_interest(int(input("Enter Interest :")))
print(sa.balance)