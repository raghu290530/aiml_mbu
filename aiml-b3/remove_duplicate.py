'''W.A.P to remove duplicate elemes in list
li = [5,6,6,9,5,9]
-> [5,6,9]'''
# n = int(input("Enter size: "))
li = list(map(int,input().split()))
unique = []
for e in li:
    if e not in unique:
        unique.append(e)
print(unique)