import pandas as pd
data = {
    "name" : ["Raghu", "Ravi","Raju"],
    "age" : [23,24,30]
}
df = pd.DataFrame(data)
print(df)
print()
print(df["name"])
print()
print(df["gae"])
print()
print(df["name"][1])