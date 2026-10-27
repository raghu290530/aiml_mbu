class Parent:
    def __init__(self,name,sal,age):
        self.name = name #public
        self._sal = sal # Protected
        self.__age = age # Private
class Child(Parent):
    def printDetails(self):
        print(self.name)
        print(self._sal)
        # print(self.__age) Error
c = Child("Raghu",20000,30)
c.printDetails()
print(c._sal)