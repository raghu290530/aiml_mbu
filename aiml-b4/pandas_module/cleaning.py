import pandas as pd

df = pd.read_csv('stu_data.csv')

# df = df.dropna()
# df = df['Age'].dropna()
# df = df.fillna(300)
df = df.fillna({"Age":300})
print(df.to_string())
