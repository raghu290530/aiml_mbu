'''Write a class Classroom with students list and a method add_student(name). Add 3 students and print the list.
'''
class Classroom:
    student_list = []
    def add_student(self,name):
        self.student_list.append(name)

c = Classroom()
c.add_student("Raghu")
c.add_student("Ravi")
c.add_student("Raju")
print(c.student_list)
