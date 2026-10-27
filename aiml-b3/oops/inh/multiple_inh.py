class A:
    x = 5
class B:
    y = 10
class D:
    a = 10
class C(A,B,D):
    z = 20
c = C()
print(c.x,c.y,c.z)
