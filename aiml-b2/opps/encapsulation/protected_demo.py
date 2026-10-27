class Parent:
    def __init__(self,pname,psal,page):
        self.pname = pname #public
        self.__psal = psal #Private
        self._page = psal   #Protected
class Child(Parent):
    def printParentDetails(self):
        print(self.pname)
        # print(self.__psal)
        print(self._page)
c = Child("Raghu",20000,10)
c.printParentDetails()
# print(super._page) errorx