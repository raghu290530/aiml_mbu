class A:
    a =20
class B(A):
    pass
class C(A):
    pass
class D(A):
    pass
b = B()
c = C()
d = D()
print(b.a,c.a,d.a)