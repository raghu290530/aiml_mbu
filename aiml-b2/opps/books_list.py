'''Write a class Book with title and author,
and a method find(author),
 and Library with a list of Book objects
 that prints all books by that author.'''
from pattren import count


class Book:
    def __init__(self,t,a):
        self.title= t
        self.author = a

li = []
n = int(input())
for i in range(n):
    bd = input().split()
    li.append(Book(bd[0],bd[1]))

author = input("Enter author name to find")

count = 0
for e in li:
    if e.author == author:
        print(e.title)
        count+=1

if count ==0:
    print("Book Not found")



