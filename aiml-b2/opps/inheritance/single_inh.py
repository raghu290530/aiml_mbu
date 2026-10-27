class A():
    x = 5
    def print(self):
        print("I am A")

class B(A):
    y = 10
    def display(self):
        print(self.x)

b = B()
b.display()
b.print()
a = A()
print(a.y)