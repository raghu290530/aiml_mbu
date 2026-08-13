n = input()
print(len(n))
print(int(n[::-1]))

ams = 0
for e in n:
    ams = ams+int(e)**3
if ams==int(n):
    print("Amstrong")
else:
    print("Not amstrong")