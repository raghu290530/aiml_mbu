'''Write a class Classroom with students list
and a method add_student(name).
Add 3 students and print the list.'''

class Classroom:
    def __init__(self):
        self.student_list = []
    def add_student(self,name):
        self.student_list.append(name)
c1 = Classroom()
c1.add_student("Raghu")
c1.add_student("Alice")
c1.add_student("Bob")
c2 = Classroom()
c2.add_student("Ravi")
c2.add_student("x")
c2.add_student("y")
c2.add_student("abc")
print(c1.student_list)
print(c2.student_list)