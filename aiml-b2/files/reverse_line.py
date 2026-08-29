'''
Write a program that reads "input.txt",
reverses the order of characters of
each line, and writes the result
to "reversed.txt".
'''
f1 = open('input.txt','rt')
f2 = open('reversed.txt','wt')
for line in f1:
    if "\n" in line:
        line = line[:len(line)-2]
    f2.write(line[::-1])
    f2.write("\n")
f2.close()
f1.close()