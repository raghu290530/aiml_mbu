def digit_word(d):
    di = {
        0:"Zero",
        1:"One",
        2:"Two",
        3:"Three"
    }
    return di[d]
n = int(input())
n = str(n)
for e in n:
    print(digit_word(int(e)),end=" ")
