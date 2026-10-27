'''Write a class GrandParent with method
 greet() printing 'Hello',
 class Parent(GrandParent),
 and class Child(Parent).
 Call greet() on Child.'''
class GrandParent:
    def greet(self):
        print("Hello")
class Parent(GrandParent):
    pass
class Child(Parent):
    pass
c = Child()
c.greet()