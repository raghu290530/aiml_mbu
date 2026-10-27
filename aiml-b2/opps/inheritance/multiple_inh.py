class A:
    x = 5
class B :
    y = 10
class D:
    z = 20
class C(A,B,D):
    pass
c = C()
print(c.x)
print(c.y)
print(c.z)