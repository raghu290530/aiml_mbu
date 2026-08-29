'''Write a class Song with title attribute.
Read two titles, create two objects,
and print 'Same' if titles are equal
else 'Different'.
'''
class Song:
    def __init__(self,title):
        self.title = title
    def compare(self,s):
        if self.title == s.title:
            print("Same")
        else:
            print("Different")
s1 = Song("Hello")
s2 = Song("Hi")
s1.compare(s2)
# if s1.title == s2.title:
#     print("Same")
# else:
#     print("Different")