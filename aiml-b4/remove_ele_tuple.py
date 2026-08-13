tp = tuple(map(int,input().split()))
ele = int(input())
if ele in tp:
    tp = list(tp)
    tp.remove(ele)
    tp = tuple(tp)
    print(tp)
else:
    print("Element not available")