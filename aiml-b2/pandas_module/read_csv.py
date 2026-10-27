import pandas as pd

df = pd.read_csv('stu_data.csv')

# df = df.dropna()
# df.dropna(inplace=True)
# df = df.fillna(300)
# df = df.fillna({"Age": 130})
df['Age'] = pd.to_numeric(df['Age'])
m = df['Age'].mean()
df = df.fillna({"Age": m})
print(df.to_string())
