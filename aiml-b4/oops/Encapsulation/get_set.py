class Employee:
    def __init__(self,name,sal):
        self.name = name
        self.__sal = sal
    def get_sal(self):
        return self.__sal
    def set_sal(self,sal):
        self.__sal = sal

c = Employee("Raghu",20000)
print("Name : ",c.name)
print("Salary : ",c.get_sal())
c.set_sal(30000)
print("Salary : ",c.get_sal())