import re

txt = "The rain in Spain"
x = re.search('r',txt)
if x:
    print("Yes")
else:
    print("No")

x = re.findall("[a]", txt)
print(x)
x = re.sub(" ", "9", txt, 2)
print(x)
print("Raghu")