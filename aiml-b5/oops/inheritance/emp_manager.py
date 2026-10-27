'''Write a class Employee with name,
and a class Manager(Employee).
Read a name and print it via the child class.'''
class Employee:
    def __init__(self,name):
        self.name = name
class Manager(Employee):
    def printName(self):
        print(self.name)

m = Manager(input())
m.printName()
# print(m.name)