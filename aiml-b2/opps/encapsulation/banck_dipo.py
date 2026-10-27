'''Write a class BankAccount with private
__balance and private __log list.
Methods deposit/withdraw append to the log.'''
class BankAccount:
    def __init__(self,balance):
        self.__balance = balance
        self.__log_list = [f'Initial Balance {self.__balance}']
    def get_balance(self):
        return self.__balance
    def get_log_list(self):
        return self.__log_list
    def deposit(self):
        a = float(input('Deposit amount: '))
        self.__balance += a
        self.__log_list.append(f'deposit {a}')
    def withdraw(self):
        a = float(input("Withdraw amount :"))
        self.__balance -= a
        self.__log_list.append(f'withdraw {a}')
ba = BankAccount(float(input()))
ba.deposit()
ba.withdraw()
print(ba.get_balance())
print(ba.get_log_list())