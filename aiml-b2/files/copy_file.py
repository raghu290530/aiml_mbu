'''WAP to copy data from one file to
another file
'file1.txt'
'file2.txt'
'''
'''Read student_data.txt file and write it
in another s_data.txt as below format
Name - Raghu
Roll_No - aiml-101
-
-
-

'''





f1 = open('file1.txt','rt')
s = f1.read()
f1.close()

f2 = open('file2.txt','wt')
f2.write(s)
f2.close()