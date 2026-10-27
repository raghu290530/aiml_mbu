class Parent:
    def __init__(self,pname,page):
        self.pname = pname
        self.page = page
    def printParentDetails(self):
        print(self.pname)
        print(self.page)

class Child(Parent):
    def __init__(self,pname,page,cname,cage):
        self.cname = cname
        self.cage = cage
        # Parent.__init__(self,pname,page)
        super().__init__(pname, page)
    def printChildDetails(self):
        print(self.cname)
        print(self.cage)
c  =Child("Raghu",30,"Child",10)
c.printChildDetails()
c.printParentDetails()

