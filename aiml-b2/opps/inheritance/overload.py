class A:
    def greet(self):
        print("Hello A")
class B(A):
    def greet(self):
        super().greet()
        print("Hello B")
b = B()
b.greet()