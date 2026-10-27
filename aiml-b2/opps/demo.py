d = "2026-09-30"
n = 2
l = d[-2]+d[-1]
l = str(int(l)+n)
d = d[:8] + l
print(d)
s  = "8985hello487"
sum = 0
for e in s:
    if e.isdigit():
        sum = sum + int(e)
print(sum)
if str(sum) == str(sum)[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")