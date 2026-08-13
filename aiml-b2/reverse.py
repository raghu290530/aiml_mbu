n = input()
print(len(n))
print(int(n[::-1]))
if n == n[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
ams = 0
for e in n:
    ams = ams + int(e)**3
if ams==int(n):
    print("Amstrong")
else:
    print("Not Amstrong")