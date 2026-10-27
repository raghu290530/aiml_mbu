import re
txt = "The rain in Spain"
x = re.findall('ab',txt)
print(x)
x = re.findall('[ab]',txt)
print(x)
x = re.findall('[abcdef]',txt)
print(x)
x = re.findall('[a-f]',txt)
print(x)
x = re.findall('[l-o]',txt)
print(x)
roll_no = "898985"
x = re.findall('[a-z]',txt)
print(x)
x = re.findall('[a-z]',roll_no)
print(x)
x = re.findall('[0-5]',roll_no)
print(x)
roll_no = 'AIML58CS001'
x=re.findall('[0-5][0-9]',roll_no)
print(x)
txt = "Hello, Heabo,Welcome,Jello,Heero,Heo"
x = re.findall('He..o',txt)
print(x)
roll_no = '25102A010141 2510AB'
x = re.findall('^2510',roll_no)
print(x)
txt = "Hello, Heabo,Welcome,Jello,Heero,Heo"
x = re.findall('He.*o',txt)
print(x)