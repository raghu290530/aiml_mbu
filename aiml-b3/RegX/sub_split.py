import re
txt  = "The rain in Spain"
x = re.split("\s",txt)
print(x)
x = re.split(" ",txt,1)
print(x)
x = re.split(" ",txt,2)
print(x)
x = re.split("rain",txt)
print(x)
x = re.split("ai",txt)
print(x)
roll_no= "2024-AIML-MBU-005"
x = re.sub('AIML','CSE',roll_no)
print(x)
roll_no= "2024-AIML-AIML-AIML-005"
x = re.sub('AIML','CSE',roll_no)
print(x)
x = re.sub('AIML','CSE',roll_no,2)
print(x)