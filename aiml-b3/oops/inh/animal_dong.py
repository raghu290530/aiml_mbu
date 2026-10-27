'''Write a base class Animal with
method speak() printing 'Animal speaks',
and a class Dog that inherits it.
Call speak() on a Dog object.'''
class Animal:
    def speak(self):
        print('Animal speaks')
class Dog(Animal):
    pass
d = Dog()
d.speak()