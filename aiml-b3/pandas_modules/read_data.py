import pandas as pd
df = pd.read_csv('stu_data.csv')
# df = df.dropna()
# df = df['City'].dropna()
# df=df.fillna(25)
df = df.fillna({'City':'Hyd'})
# x = df['Age'].mode()[0]
x = df['Age'].mean()
# x = df['Age'].median()
df = df.fillna({'Age':x})
df.loc[5,'Age'] = 20
print(df.to_string())