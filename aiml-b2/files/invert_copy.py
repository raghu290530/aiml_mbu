'''Read student_data.txt file and write it
in another s_data.txt as below format
Name - Raghu
Roll_No - aiml-101
-
-
-

'''

f1 = open('student_data.txt','rt')
k = f1.readline().split()
v = f1.readline().split()
f1.close()

f2 = open('s_data.txt','wt')

for i in range(len(k)):
    f2.write(f"{k[i]} - {v[i]}\n")
f2.close()







