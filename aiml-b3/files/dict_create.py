'''WAP to create a dict from a given file
"list_data.txt"'''
f = open('list_data.txt','rt')
names = f.readline().split()
ages = list(map(int,f.readline().split()))
di = {}
for i in range(len(names)):
    di[names[i]] = ages[i]
print(di)