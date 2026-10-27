'''Write a class Player with name and score.
Read N players, create objects in a list,
and print the name of the highest scorer.'''
import pattren

class Player:
    def __init__(self,name,score):
        self.name = name
        self.score = score

n = int(input())
playerlist = []
for i in range(n):
    p = input().split()
    playerlist.append(Player(p[0],int(p[1])))
m = playerlist[0]
for i in range(1,n):
    if playerlist[i].score > m.score:
        m = playerlist[i]
print(m.name)