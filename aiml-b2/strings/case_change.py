'''Write a program to swap the case of each character (lower to upper and vice versa) in the given string.
'''
def swap_char(s):
    s1 = ""
    for i in range(len(s)):
        if s[i].islower():
            s1=s1+s[i].upper()
        else:
            s1 = s1 + s[i].lower()
    return s1
print(swap_char("gfjhgh"))
