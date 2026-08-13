s = input()
print("Length ", len(s))
print("Reverse ", s[::-1])
def is_palindrome(s1):
    if s1 == s1[::-1]:
        return True
    return False
print("Is Palindrome = ",is_palindrome(s))

def sum_digits(s1):
    sum = 0
    for d in s1:
        sum = sum+int(d)
    return sum
print("sum = ",sum_digits(s))

def is_amstrong(s1):
    ams = 0
    for d in s1:
        ams = ams + int(d)**len(s1)
    if ams == int(s1):
        return True
    return False
print(is_amstrong(s))
n1 = int(input())
n2 = int(input())
for i in range(n1,n2+1):
    if is_amstrong(str(i)):
        print(i)
