'''Write a class Phone with attribute battery.
 Create an object with battery 100,
 read a new value, update it, and print it.'''
class Phone:
    def __init__(self,battery):
        self.battery = battery

p = Phone(100)
print(f"{p.battery}%")
p.battery = int(input())
print(f"{p.battery}%")