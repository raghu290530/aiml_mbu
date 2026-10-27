'''Write a class Bird with method fly()
printing 'Flying', and class Eagle(Bird).
Create an Eagle object and call fly().'''
class Bird:
    def fly(self):
        print('Flying')
class Eagle(Bird):
    pass
e = Eagle()
e.fly()