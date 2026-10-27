'''Child having init method but not Parent'''
class Parent:
    pass

class Child(Parent):
    def __init__(self,cname,csal):
        self.cname = cname
        self.csal =csal
    def printDetails(self):
        print("P Name:",self.cname)
        print("P Sal: ",self.csal)

c = Child("Raghu",20000)
c.printDetails()