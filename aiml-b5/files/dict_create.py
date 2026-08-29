'''WAP to read data from file
- dict_data.txt
first lines - keys (str)
second line - values(int)
create a dict using above file
'''
f = open('dict_data.txt','rt')
k = f.readline().split()
v = list(map(int,f.readline().split()))
di = {}
for i in range(len(k)):
    di[k[i]] = v[i]
print(di)