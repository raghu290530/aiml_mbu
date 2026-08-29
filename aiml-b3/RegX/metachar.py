import  re
txt = "The rain in Spain"
x = re.findall('[api]',txt)
print(x)
x = re.findall('[a-o]',txt)
print(x)