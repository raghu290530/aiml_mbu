'''Write a class Classroom with students list
 and a method add_student(name).
 Add 3 students and print the list.'''

class Classroom:
    def __init__(self):
        self.student_list = []
    def add_student(self,name):
        self.student_list.append(name)

c1 = Classroom()
c1.add_student(input())
c1.add_student(input())
c1.add_student(input())
print(c1.student_list)