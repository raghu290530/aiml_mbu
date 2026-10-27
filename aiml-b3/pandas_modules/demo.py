import pandas
data = {
    'name' : ["Raghu","Ravi","Raju"],
    'age' : [45,34,26]
}
df = pandas.DataFrame(data)
print(df)
print(df['age'])
print(df['name'][2])