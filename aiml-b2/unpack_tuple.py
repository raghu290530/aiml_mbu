tp = (5,6,9)
a,b,c = tp
print(a,b,c)

tp2 = (5,9,6,8,"Raghu",2.5)
# a1,b1,c1 = tp2  error
a1,b1,*c1 = tp2
print(a1,b1,c1)

a2,*b2,c2 = tp2
print(a2,b2,c2)

tp3 = (5,6)
a3,b3,c3 = tp3
print(a3,b3,c3)