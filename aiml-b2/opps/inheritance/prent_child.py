class Parent:
    def __init__(self,name,age):
        self.pname = name
        self.page = age

class Child(Parent):
    def display(self):
        print("Name : ",self.pname)
        print("Age : ",self.page)

c = Child("Raghu",30)
c.display()
