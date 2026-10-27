'''Write a class Account with private __balance
and a method transfer(other, amount) that
only works if the balance is sufficient.
Input Format
First line: balance of A.
Second line: balance of B.
Third line: amount'''
class Account:
    def __init__(self,balance):
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def transfer(self,other,amount):
        if(self.__balance>=amount):
            self.__balance -=amount
            other.__balance += amount
            print("Transaction Successful")
            print(self.__balance)
            print(other.__balance)
        else:
            print('Insufficient balance')
a = Account(float(input()))
b = Account(float(input()))
a.transfer(b,float(input()))