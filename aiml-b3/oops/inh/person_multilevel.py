'''Write classes Person(name),
Student(Person) adding grade,
and Scholar(Student) adding scholarship amount.'''
class Person:
    def __init__(self,name):
        self.name = name
class Student(Person):
    def __init__(self,name,grade):
        self.grade =grade
        super().__init__(name)
class Scholar(Student):
    def __init__(self,name,grade,amount):
        self.amount = amount
        super().__init__(name,grade)

sc = Scholar("Raghu","A",20000)
print(sc.name)
print(sc.amount)
print(sc.grade)