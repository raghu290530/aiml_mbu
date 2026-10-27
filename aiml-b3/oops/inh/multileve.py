class A:
    x = 5
class B(A) :
    y = 10
class C(B):
    z = 20
c = C()
print(c.x)
print(c.y)
print(c.z)