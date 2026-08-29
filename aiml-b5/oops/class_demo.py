class Student:
    def __init__(self,name,age):
        self.name =name
        self.age = age
    def greet(self):
        print("Hello ",self.name,"!!!")

s1 = Student("Raghu", 30)
s1.greet()