'''Write a class Laptop with brand,
 and a class GamingLaptop(Laptop)
 with extra attribute rgb = True.
 Print both.'''
class Laptop:
    def __init__(self,b):
        self.brand = b
class GamingLaptop(Laptop):
    def __init__(self,b):
        self.rgb = True
        Laptop.__init__(self,b)
    def printDetalis(self):
        print(self.brand)
        print(self.rgb)
gl = GamingLaptop(input())
gl.printDetalis()