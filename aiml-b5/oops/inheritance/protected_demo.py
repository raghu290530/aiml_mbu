class Parent:
    def __init__(self,name,sal,age):
        self.name = name #Public
        self.__sal = sal #Private
        self._age =age  #Protected
    def __greet(self):
        print("Greet")
    def _pro(self):
        print("Protected")
class Child(Parent):
    def display(self):
        print(self.name)
        # print(self.__sal)
        print(self._age)
c = Child("Raghu",20000,30)
c.display()
# c.__greet() error
c._pro()