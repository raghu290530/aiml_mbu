f = open('data.txt','rt')
count = 0
for line in f:
    count += 1
f.close()
print(count)