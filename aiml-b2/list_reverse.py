'''input and print in reverse order'''
n = int(input())
li = []
for i in range(n):
    li.append(int(input()))

print("Normal : ",li)
# li.reverse()
# print("Reverse :",li)
print("Reverse :",li[::-1])