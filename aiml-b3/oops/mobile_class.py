'''Create a class called Mobile with follwing
properties - brad, model,year and create 2 objects
and print the details'''
from xxsubtype import bench


class Mobile:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
    def display(self):
        print("Brand ", self.brand)
        print("Model ",self.model)
        print("Year ",self.year)

m1 = Mobile("Oppo","A5",2023)
m2 = Mobile("Nokia","Z",2025)
m1.display()
m2.display()
