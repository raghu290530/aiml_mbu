'''Write classes A, B(A), C(B).
Give A a method hello() and call it on
a C object.'''
class A:
    def hello(self):
        print("Hello from A")
class B(A):
    pass
class C(B):
    pass
c = C()
c.hello()