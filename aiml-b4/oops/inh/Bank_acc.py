'''Write a class BankAccount with balance
and deposit(), and a class
SavingsAccount(BankAccount) with
apply_interest(rate).'''
class BankAccount:
    def __init__(self,balance):
        self.balance = balance
    def deposit(self):
        d = float(input("Enter Diposit amount :"))
        self.balance += d
class SavingsAccount(BankAccount):
    def apply_intrest(self,rate):
        self.balance += self.balance*rate/100
sa = SavingsAccount(float(input("Enter Balance")))
sa.deposit()
sa.apply_intrest(float(input("Enter rate:")))
print(sa.balance)

