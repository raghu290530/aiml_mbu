'''W.A.P to read integer data
 from the file 'int_data.txt'
and find maximum number'''
f = open('int_data.txt','rt')
s = f.read()
li = list(map(float,s.split()))
print("Max -" , max(li))