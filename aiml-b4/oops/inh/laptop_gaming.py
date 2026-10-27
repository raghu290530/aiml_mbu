'''Write a class Laptop with brand,
and a class GamingLaptop(Laptop)
with extra attribute rgb = True. Print both.'''
class Laptop:
    def __init__(self,brand):
        self.brand = brand
class GamingLaptop(Laptop):
    def __init__(self,brand):
        self.rgb = True
        super().__init__(brand)
    def display(self):
        print(self.brand)
        print(self.rgb)
gl = GamingLaptop(input())
gl.display()