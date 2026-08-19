s = input()

def str_len(s):
    return len(s)

def str_rev(s):
    return s[::-1]

def is_palindrome(s):
    if s == str_rev(s):
        return True
    return False

print(str_len(s))
print(str_rev(s))
print(is_palindrome(s))

for ch in s:
    print(ch)