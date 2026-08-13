def remove_space(s):
    li = s.split()
    line = ""
    for e in li:
        line += e
    return line
s = "I am Raghu"
print(remove_space(s))
def count_words(s):
    return len(s.split())
print("Count = ",count_words(s))