class Parent:
    def __init__(self,pname,page):
        self.pname = pname
        self.page = page

class Child(Parent):
    def printDetails(self):
        print(self.pname)
        print(self.page)
c  =Child("Raghu",30)
c.printDetails()
