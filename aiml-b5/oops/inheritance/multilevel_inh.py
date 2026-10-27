'''Multilevel Inh'''
class A:
    x = 5
    def greet(self):
        print("Hello A")
class B(A):
    y = 10
class C(B):
    z = 20
c = C()
print(c.x, c.y, c.z)
c.greet()
