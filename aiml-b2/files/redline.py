f = open('demo.txt','rt')
l = f.readline() #one line
print(l)
l = f.readline()
print(l)
l = f.readline()
print(l)
l = f.read(5)  #5 char
print(l)
f.close()