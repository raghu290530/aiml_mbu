import re
txt = "Hello, Heabo, Jello, World, Heuiuhgjhg"
x = re.findall('He..o',txt)
print(x)
x = re.findall('He...',txt)
print(x)
x = re.findall('.....',txt)
print(x)
x = re.findall('^He',txt)
print(x)