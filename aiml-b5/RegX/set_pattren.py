import re
txt = "The rain in Spain 2025"
x = re.findall('[abi]',txt)
print(x)
x = re.findall('[abcdefghijk]',txt)
print(x)
x = re.findall('[a-k]',txt)
print(x)
x = re.findall('[Sn]',txt)
print(x)
x = re.findall('[0-9]',txt)
print(x)
x = re.findall('[68]',txt)
print(x)
x = re.findall('[a-zA-Z]',txt)
print(x)
x = re.findall('[A-Z][a-z]',txt)
print(x)
mail = "raghu@gmail.com"
x = re.findall('@',mail)
print(x)
pwd = "abc$123@"
x = re.findall('[$@/!]',pwd)
print(x)
# roll_no = "2024-AIML-MBU-005"
