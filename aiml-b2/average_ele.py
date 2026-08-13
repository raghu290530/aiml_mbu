n = int(input())
li = []
for i in range(n):
    li.append(int(input()))
avg = sum(li)/len(li)
li2 = []
for i in range(len(li)):
    if li[i]>avg:
        li2.append(li[i])
print(li2)