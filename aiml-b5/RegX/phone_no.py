import re
mn = input()
if re.findall('^\+91[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]',mn) and len(mn)==13:
    print("Valid")
elif re.findall('[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]',mn) and len(mn)==10:
    print("Valid")
else:
    print("Invalid")