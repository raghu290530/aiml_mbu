name = input()
print(name[::-1])
print(len(name))
if name == name[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
sum = 0
ams = 0
# for e in name:
#     sum = sum + int(e)
#     ams = ams + int(e)**3
print(sum)
print(ams)
print(len(name.split()))