import re
pwd = input()
lv = uv = dv = lenv = spv = swv = False
if re.findall('[a-z]',pwd):
    lv = True
if re.findall('[A-Z]',pwd):
    uv = True
if re.findall('[0-9]',pwd):
    dv = True
if len(pwd)>=3 and len(pwd)<=8:
    lenv = True
if re.findall('[@$!#]',pwd):
    spv = True
if re.findall('^[a-zA-Z]',pwd):
    swv = True
if lv and uv and dv and lenv and spv and swv:
    print("Valid")
else:
    print("Invalid")
print('1 Lower Case : ',lv)
print('1 Upper Case : ',uv)
print('1 Digit : ',dv)
print('Length check : ',lenv)
print('1 Special Char : ',spv)
print('Starts with Char: ',swv)
