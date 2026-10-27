class A:
    x = 5
class B(A):
    pass
class C(A):
    pass
class D(A):
    pass
b = B()
print(b.x)
c = C()
print(c.x)
d = D()
print(d.x)