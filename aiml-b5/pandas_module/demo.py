#pip install pandas
import pandas as pd
data = {
    'name' : ["Raghu","Ravi","Raju"],
    'age' : [25,24,26]
}
df = pd.DataFrame(data)
print(df)
print(df['name'])
print(df['name'][2])
print(df.loc[1,'age'])
print(df.loc[0])