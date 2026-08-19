'''Create class variables and assign using init'''
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name = ",self.name)
        print("Age = ",self.age)

s1 = Student("Raghu",30)
s1.display()
s2 = Student("Raju",20)
s2.display()