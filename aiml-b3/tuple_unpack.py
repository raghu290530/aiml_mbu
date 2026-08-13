'''
tp = (5,8,9)
a,b,c = tp
print(a,b,c)
'''

tp2 = (9,8,4,3,5)
#a,b,c = tp2 # error
a,*b,c = tp2
print(a,b,c)

tp3 = (5,6)
e,d,f = tp3