'''find the sum of digits availble in a string
and check is palindrome
s = '456He8llo5'
'''
s = '456He8llo55'
sum = 0
for e in s:
    if e.isdigit():
        sum += int(e)
if str(sum) == str(sum)[::-1]:
    print(sum,"Palindrome")
else:
    print(sum,"Not Palindrome")