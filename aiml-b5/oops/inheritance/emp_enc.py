'''Write a class Employee with private
__name and __salary and getters/setters
for both.'''
class Employee:
    def __init__(self,name,sal):
        self.__name = name
        self.__salary = sal
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    def get_salary(self):
        return self.__salary
    def set_salary(self,sal):
        self.__salary = sal
e = Employee(input(),float(input()))
print(e.get_name())
print(e.get_salary())