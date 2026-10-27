class Student:
    def __init__(self,name,roll_no,avg):
        self.name = name
        self.roll_no = roll_no
        self.avg = avg
    def display(self):
        print("Name = ",self.name)
        print("Roll No = ",self.roll_no)
        print("Avg = ",self.avg)
s1 = Student("Raghu",123,67.9)
s1.display()
s2 = Student("Raju",456,87.6)
s2.display()