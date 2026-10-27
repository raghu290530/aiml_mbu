class Student:
    def __init__(self,name,avg):
        self.name = name
        self.__avg = avg  #private variable

    def get_avg(self):
        return self.__avg

    def set_avg(self,avg):
        self.__avg = avg
s  = Student("Raghu",86.5)
print(s.name)
# print(s.__avg) error
print(s.get_avg())
# s.__avg = 46.8
s.set_avg(46.8)
print(s.get_avg())