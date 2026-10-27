'''Write a class Employee with private
 __name and __salary and getters/setters
 for both.
'''
class Employee:
    def __init__(self,n,s):
        self.__name = n
        self.__sal = s
    def get_name(self):
        return self.__name
    def get_sal(self):
        return self.__sal
    def set_name(self,n):
        self.__name = n
    def set_sal(self,s):
        self.__sal = s
e = Employee(input(),float(input()))
print(e.get_sal())
print(e.get_name())