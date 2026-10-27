import re
c = input()
if(len(c)==4 and re.search("[A-M][I-Z][0-5][5-9]",c)):
    print("Yes")
else:
    print("NO")
