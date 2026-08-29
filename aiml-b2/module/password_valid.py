import re
pwd = input()
sw = ln = digit = low = upp = False
if re.search('^[a-zA-Z]',pwd):
    sw = True
if len(pwd)>=3 and len(pwd)<=8:
    ln = True
if re.search('[0-9]',pwd):
    digit = True
if re.search('[a-z]',pwd):
    low = True
if re.search('[A-Z]',pwd):
    upp = True
if(sw and ln and digit and low and upp):
    print("Password is valid")
else:
    print("Password is Invalid")
print(f"Starts with Char : {sw}")
print(f"Length must be >=3 and <=8 : {ln}")