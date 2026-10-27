from unittest.mock import inplace

import pandas as pd
df = pd.read_csv('stu_data.csv')
df = df.drop_duplicates()
# df = df.dropna()
# df = df.fillna(300)
# df = df.fillna({'Age':300})
# m = df['Age'].mean()
# m = df['Age'].median()
m = df['Age'].mode()[0]
df = df.fillna({'Age':m})
m = df['City'].mode()[0]
df = df.fillna({'City':m})
df.loc[5,'Age'] = 20
df.loc[7,'Marks'] = '70'
# df['Marks']=df.to_nu['Marks'].to_number()
m = df['Marks'].mean()
print(m)
print(df.to_string())