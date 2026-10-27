import re
pwd = input()
swv = lv = uv = dv = spcv = lenv = False
if re.findall('^[a-zA-Z]',pwd):
    swv = True
if re.findall('[a-z]',pwd):
    lv = True
if re.findall('[A-Z]',pwd):
    uv = True
if re.findall('[0-9]',pwd):
    dv = True
if re.findall('[@$#!]',pwd):
    spcv = True
if len(pwd)>=4 and len(pwd)<=8:
    lenv = True

if lv and uv and lenv and spcv and dv and swv:
    print("Valid")
else:
    print("Invalid")

print("Starts with : ",swv)
print("1 Lower Case: ",lv)
print("1 Upper Case: ",uv)
print("1 Digit : ",dv)
print("Length : ",lenv)
print("1 Special: ",spcv)
