'''WAP to copy one file data to
another file
file1.txt -> file2.txt
'''

f1 = open('file1.txt','rt')
s = f1.read()
f1.close()

f2 = open('file2.txt','wt')
f2.write(s)
f2.close()