import re
roll_no = '2024AIML005'
txt = "The rain in Spain"
x = re.findall('[A]',roll_no)
print(x)
x1 = re.findall('[zS]',txt)
print(x1)
x2 = re.findall('[m-z]',txt)
print(x2)
x3 = re.findall('[MLAI]',roll_no)
print(x3)
x3 = re.findall('[a-zA-Z\b]',roll_no)
print(x3)

txt = "Hello , Herao, World"
x = re.findall("He..o",txt)
print(x)

x = re.findall('^2026',roll_no)
print(x)
var1= 'Sub1'
x = re.findall('^[a-zA-Z]',var1)
print(x)
x = re.findall('005$',roll_no)
print(x)
# x = re.findall('\d',txt)
# print(x)
print("Raghu\b")