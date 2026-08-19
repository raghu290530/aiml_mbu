class Message:
    def __init__(self,name):
        self.name = name
    def greet(self):
        print("Welcome ", self.name)

m1 = Message("Raghu")
m1.greet()
m1.greet()