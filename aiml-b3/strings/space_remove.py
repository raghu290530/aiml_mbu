'''Write a program to remove all whitespace characters from the given string.
'''

def remove_spaces(s):
    s = s.replace(" ","")
    return s
print(remove_spaces(input()))

'''Write a program to count the number of words in the given string. Words are separated by single spaces.
'''

def no_of_words(s):
    li = s.split()
    print(li)
    return len(li)
print(no_of_words("jkasdha jkhsdkas dkjashdk as"))