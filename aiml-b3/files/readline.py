f = open("demo.txt","rt")
l = f.readline()  #only one line
print(l)
l = f.readline()
print(l)
l = f.readline()
print(l)
l = f.read(5) #only first 5 char
print(l)

f.close()