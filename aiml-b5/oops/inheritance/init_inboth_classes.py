class Parent:
    def __init__(self, pname, psal):
        self.pname = pname
        self.psal = psal
    def printPDetails(self):
        print("P Name:",self.pname)
        print("P Sal: ",self.psal)

class Child(Parent):
    def __init__(self,pname,psal,cname,csal):
        self.cname = cname
        self.csal =csal
        Parent.__init__(self,pname,psal)
        # super().__init__(pname,psal)
    def printCDetails(self):
        print("P Name:",self.cname)
        print("P Sal: ",self.csal)

c = Child("Raghu",20000,"Ravi",10000)
c.printCDetails()
c.printPDetails()