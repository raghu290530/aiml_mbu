'''Parent having init method but not child'''
class Parent:
    def __init__(self,pname,psal):
        self.pname = pname
        self.psal =psal
class Child(Parent):
    def printDetails(self):
        print("P Name:",self.pname)
        print("P Sal: ",self.psal)

c = Child("Raghu",20000)
c.printDetails()