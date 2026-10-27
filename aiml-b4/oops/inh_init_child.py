class Parent:
    pass

class Child(Parent):
    def __init__(self,cname,cage):
        self.cname = cname
        self.cage = cage
    def printDetails(self):
        print(self.cname)
        print(self.cage)
c  =Child("Raghu",30)
c.printDetails()
