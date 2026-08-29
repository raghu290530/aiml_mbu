f = open('student_data.txt','rt')
k = f.readline().split()
v = f.readline().split()
di = { }
for i in range(len(k)):
    if(i>=2):
        di[k[i]] = int(v[i])
    else:
        di[k[i]] = v[i]
print(di)