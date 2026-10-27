'''Single Inh'''
class A:
    x = 5
    def greet(self):
        print("Hello from A")
class B(A):
    y = 10

b = B()
print(b.y)
print(b.x)
b.greet()
a = A()
