class A:
    def greet(self):
        print("Hello from A")
class B(A):
    def greet(self):
        print("Hello from B")
b = B()
b.greet()