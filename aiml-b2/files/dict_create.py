'''WAP to create a dict from a given file
"list_data.txt"
first line - keys (str)
second line - Values(int)
"'''
f = open('list_data.txt','rt')
k = f.readline().split()
v = list(map(int,f.readline().split()))
di = { }
for i in range(len(k)):
    di[k[i]] = v[i]
print(di)
