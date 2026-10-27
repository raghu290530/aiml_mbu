class Student:
    def __init__(self,name,avg):
        self.name = name #public
        self.__avg = avg # Private
    def printAvg(self):
        print(self.__avg)
    def __details(self): #Private Method
        print("Raghu")
s = Student("Raghu",85)
print(s.name)
s.printAvg()
s.details()