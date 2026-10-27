class A:
    x = 5
class B:
    y = 10
class D:
    z = 50

class C(A,B,D):
    pass
c = C()
print(c.x,c.y)