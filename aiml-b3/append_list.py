'''w.a.p to input size n, and input n no of elemets (int)
and create a list and print the list in both normal and reverse  order'''
n = int(input("Enter size: "))
li = []
for i in range(n):
    li.append(int(input()))
print("Normal : ", li)
# li.reverse()
print("Revese : ", li[::-1])