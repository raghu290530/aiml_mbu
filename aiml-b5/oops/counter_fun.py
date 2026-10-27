class CounterDemo:
    def __init__(self):
        self.count = 0
    def inc(self):
        self.count +=1
    def dec(self):
        self.count -=1
    def print_count(self):
        print(self.count)
    def reset(self):
        self.count = 0
c = CounterDemo()
while True:
    n = int(input("1-inc\n2-dec\n3-print\n4-reset\n0-Exit\n"))
    match n:
        case 1: c.inc()
        case 2: c.dec()
        case 3: c.print_count()
        case 4: c.reset()
        case 0: break
# c.print_count()
# c.inc()
# c.inc()
# c.print_count()
# c.dec()
# c.dec()
# c.dec()
# c.print_count()