''' create 2 classes
1) class A -> x = 5
2) class B -> y =10
create seperate objects and print the above values
'''
class A:#Parent
    x = 5
    def greet(self):
        print("Hello A")
class B(A):#Child class
    y = 10
b = B()
print(b.y)
print(b.x)
b.greet()
a = A()
# print(a.y)