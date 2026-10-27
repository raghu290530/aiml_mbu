'''Write a class Employee with name,
and a class Manager(Employee).
Read a name and print it via the child class.'''
class Employee:
    def __init__(self,name):
        self.name = name
class Manger(Employee):
    pass
m = Manger(input())
print(m.name)