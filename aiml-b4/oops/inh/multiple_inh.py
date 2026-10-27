class A:
    a = 10
class B:
    b = 20
class D:
    d = 50
class C(A,B,D):
    pass

c = C()
print(c.a,c.b,c.d)