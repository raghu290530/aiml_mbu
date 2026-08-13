'''Given a list of integers, find the
sum, max, min, len of all elements in the list'''
n = int(input("Enter size: "))
li = []
for i in range(n):
    li.append(int(input()))
print("Sum : ", sum(li))
print("Max : ", max(li))
print("Min : ", min(li))
print("Len : ", len(li))

