class Parent:
    def __init__(self,pname,page):
        self.pname = pname
        self.page = page
    def pdisplay(self):
        print("PName : ",self.pname)
        print("PAge : ",self.page)


class Child(Parent):
    def __init__(self,pname,page,cname,cage):
        self.cname = cname
        self.cage = cage
        Parent.__init__(self,pname,page)
        # super().__init__(pname, page)
    def cdisplay(self):
        print("CName : ",self.cname)
        print("CAge : ",self.cage)

c = Child("Raghu",30,"Advitha",4)
c.cdisplay()
c.pdisplay()
