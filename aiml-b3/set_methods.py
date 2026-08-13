s1 = {5,6,6,9,10}
s2 = {6,4,8,9}
# s1.update(s2)
# s3 = s1.union(s2)

s3=s1.intersection(s2)
print(s3)
s4 = s1.difference(s2)
print(s4)
s5 = s1.symmetric_difference(s2)
print(s5)