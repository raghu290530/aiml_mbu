'''Write a class Movie with
title attribute and a method get_title()
that returns it.
'''
class Movie:
    def __init__(self,title):
        self.title = title
    def get_title(self):
        return self.title
m = Movie(input("Enter Movie:"))
print(m.get_title())