try:
    n = int(input())
    li = list(map(int,input().split()))
    i=0
    while i<n:
        print(li[i])
        i+=1
except IndexError:
    print("Enter no of elements equal to n")
except ValueError:
    print("Enter only integers")
