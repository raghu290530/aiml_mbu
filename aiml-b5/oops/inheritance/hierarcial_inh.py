class A:# Parent
    x = 5
class B(A):
    pass
class C(A):
    pass
class D(A):
    pass
b = B()
c = C()
d = D()
print(b.x,c.x,d.x)