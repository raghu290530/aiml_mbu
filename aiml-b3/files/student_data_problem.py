'''W.A.P to read studnet data and calculate total
copy name,roll no, totoal in to new file'''

f1 = open('student_data.txt','rt')
f2 = open('total_data.txt','wt')
li = []
f2.write(f"{'Name':<10} {'Roll_No':<10} {"Total":<10}\n")
f2.write("--------------------------------------------\n")
for line in f1:
    data = line.split()
    f2.write(f"{data[0]:<10} {data[1]:<10} {sum(list(map(int,data[2:]))):<10}\n")