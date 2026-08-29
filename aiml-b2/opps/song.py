'''Write a class Song with title attribute.
Read two titles, create two objects,
and print 'Same' if titles are equal
else 'Different'.'''
class Song:
    def __init__(self,title):
        self.title = title
    def is_equal(self,s):
        if self.title == s.title:
            print("Same")
        else:
            print("Different")

s1 = Song("Hi")
s2 = Song("Hello")
s1.is_equal(s2)
s = "i am raghu"
# if s1.title == s2.title:
#     print("Same")
# else:
#     print("Different")