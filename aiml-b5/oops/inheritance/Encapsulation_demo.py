class Student:
    def __init__(self,name,avg):
        self.name = name
        self.__avg = avg #Private
    def get_avg(self):
        return self.__avg
    def set_avg(self,avg):
        self.__avg = avg
s = Student("Raghu",78.6)
print(s.name)
# print(s.__avg) error
print(s.get_avg())
s.set_avg(45.8)
print(s.get_avg())