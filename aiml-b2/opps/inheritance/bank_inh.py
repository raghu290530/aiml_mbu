'''Write a class BankAccount with balance and
deposit(), and a class SavingsAccount(BankAccount)
 with apply_interest(rate).'''
class BankAccount:
    def __init__(self,b):
        self.balance  = b
    def deposit(self):
        d = float(input("Enter Deposit Amount : "))
        self.balance+=d

class SavingsAccount(BankAccount):
    def apply_interest(self,rate):
        self.balance += self.balance*rate/100
sa = SavingsAccount(float(input("Enter Balance : ")))
sa.deposit()
sa.apply_interest(float(input("Enter rate of Interest : ")))
print(sa.balance)
'''Write a class Animal with speak() printing 
'Animal speaks', and a class Dog(Animal) that 
overrides speak() to first call super().speak() 
then print 'Dog barks'.'''