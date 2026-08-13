'''Given a list of integers, count how many
even numbers, odd nos and prime numbers are present.'''
n = int(input("Enter size: "))
li = []
for i in range(n):
    li.append(int(input()))

e_count = 0
o_count = 0
p_count = 0
for e in li:
    if e%2==0:
        e_count +=1
    else:
        o_count +=1
    isprime = True
    for i in range(2,e//2+1):
        if e%i == 0:
            isprime = False
            break
    if e==2: isprime=True
    if e==1: isprime=False
    if isprime==True:
        print(e)
        p_count += 1
print("Even count",e_count)
print("Odd count",o_count)
print("Prime count",p_count)