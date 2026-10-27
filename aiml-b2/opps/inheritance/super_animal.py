'''Write a class Animal with speak() printing
'Animal speaks', and a class Dog(Animal) that
overrides speak() to first call super().speak()
then print 'Dog barks'.'''
class Animal:
    def speak(self):
        print('Animal speaks')
class Dog(Animal):
    def speak(self):
        super().speak()
        print('Dog barks')
d = Dog()
d.speak()