'''Write a class Math with a method
add(a, b, c=0) that works with 2 or 3
arguments.
'''
class Math:
    def add(self,a,b,c=0):
        d = c-a
        print(a+b+c)
m = Math()
x,y = map(int,input().split())
a,b,c = map(int,input().split())
m.add(x,y)
m.add(a,b,c)