f = open("student_data.txt","rt")
data = {}
for line in f:
    line = line.split()
    data[line[1]] = {
        'name' : line[0],
        's1' : int(line[2]),
        's2': int(line[3]),
        's3': int(line[4]),
        's4': int(line[5]),
        's5': int(line[6]),
        'total' : sum(list(map(int,line[2:]))),
    }

# print(data)
total_list = []
for k in data:
    total_list.append(data[k]['total'])
print(total_list)
for k in  data:
    if data[k]['total'] == max(total_list):
        print(data[k])