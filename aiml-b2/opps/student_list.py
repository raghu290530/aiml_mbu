'''
create a class Classroom with student_list
and perform follwing operations
1. add_student(name,roll_no,avg)
    - added {roll no} sucessfully
2 remove_student(roll_no)
    - removed the student {roll no}
3 disply_all_students()
    - list of studnets with format
    Roll_no  Name  Average
4 update_name(roll_no)
5 disply_single_student(roll_no)
    - student not available
'''

class Classroom:
    s_list = { }
    def add_student(self,name,roll_no,avg):
        self.s_list[roll_no] = [name,avg]
    def disply_list(self):
        print(f"{'Name':<15}{'Roll No':<15}{'Average':<15}")
        print("-------------------------------------")
        for k in self.s_list:
            print(f"{self.s_list[k][0]:<15}{k:<15}{self.s_list[k][1]:<15}")
    def disply_single_student(self,roll_no):
        if roll_no in self.s_list:
            print(f"{'Name':<15} {'Roll No':<15} {'Average':<15}")
            print("-------------------------------------")
            print(f"{self.s_list[roll_no][0]:<15}{roll_no:<15}{self.s_list[roll_no][1]:<15}")
        else:
            print("Invalid rollno")
    def remove_student(self,roll_no):
        if roll_no in self.s_list:
            name = self.s_list.pop(roll_no)
            print(f"{roll_no} - {name[0]} is removed")

        else:
            print("Invalid rollno")
    def update_name(self,roll_no):
        if roll_no in self.s_list:
            name = input("Enter New Name : ")
            self.s_list[roll_no][0] = name
            print(f"{roll_no} name is updated to {name}")

c1 = Classroom()
while True:
    print("1-Add\n2-List\n3-Remove\n4-Update\n0-exit")
    op = int(input("Enter your option : "))
    match(op):
        case 1 : c1.add_student(input("Enter Name: "),input("Enter Roll no"),float(input("Enter Average")))
        case 2 : c1.disply_list()
        case 3 : c1.remove_student(input("Enter Roll no: "))
        case 4 : c1.update_name(input("Enter Roll no : "))
        case _: print("Exit");break;


