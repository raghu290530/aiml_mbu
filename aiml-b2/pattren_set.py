se = {5,9,6,3}
for e in se:
    print(e, ":")
    for i in range(e+1):
        for j in  range(i):
            print("*",end = " ")
        print()
