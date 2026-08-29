import re
txt  = "The rain in Spain"
x = re.findall("raghu",txt)
print(x)
x = re.findall("rain",txt)
print(x)
x = re.findall("ai",txt)
print(x)
x = re.search("raghu",txt)
print(x)
x = re.search("rain",txt)
print(x)
x = re.search("ai",txt)
print(x)