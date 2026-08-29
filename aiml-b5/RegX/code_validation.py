import re
code = input()
if(len(code)==4 and re.findall('[A-N][O-Z][0-3][5-9]',code)):
    print("Valid")
else:
    print("In Valid")
