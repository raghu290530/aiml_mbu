'''Write a class Player with name and score.
Read N players, create objects in a list,
and print the name of the highest scorer.'''
class Player:
    def __init__(self,name,score):
        self.name = name
        self.score = score

li = []
n = int(input())
for i in range(n):
    p = input().split()
    li.append(Player(p[0],int(p[1])))

max_p = li[0].name
max = li[0].score
for e in li:
    if e.score>max:
        max = e.score
        max_p = e.name
print(max_p)