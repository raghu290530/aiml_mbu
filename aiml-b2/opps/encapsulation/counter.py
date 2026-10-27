'''Write a class Counter with private
__count and methods increment(), reset(),
and get_count().
'''
class Counter:
    def __init__(self):
        self.__count = 0
    def increment(self):
        self.__count +=1
    def reset(self):
        self.__count = 0
    def get_count(self):
        return self.__count
c = Counter()
print(c.get_count())
c.increment()
c.increment()
c.increment()
print(c.get_count())
c.reset()
print(c.get_count())