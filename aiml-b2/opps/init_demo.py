class Student:
    def __init__(self,name,age):
        self.name = name
        self.age =age
        gender = "Male"
s1 = Student("Raghu",30)
print(s1.age)
print(s1.name)
s2 = Student("Raju", 20)
print(s2.age)
print(s2.name)
print(s2.gender)