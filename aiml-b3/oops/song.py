'''Write a class Song with title attribute.
Read two titles, create two objects, and print 'Same' if titles are equal else 'Different'.'''

class Song:
    def __init__(self,title):
        self.title = title

s1 = Song("Hello")
s2 = Song("Hello")
if s1.title == s2.title:
    print("Equal")
else:
    print("Diffrent")