import pandas as pd
import numpy as np

df = pd.read_json('test.json', encoding="utf-8", orient='records')
df.fillna('空', inplace=False)
# df['avatar'] = df['avatar'].apply(lambda x: ','.join('%s' %id for id in x))
df['avatar'] = df['avatar'].apply(lambda x: ''.join(x))
df['name'] = df['name'].apply(lambda x: ''.join(x))
df['doctor_title'] = df['doctor_title'].apply(lambda x: x if pd.isnull(x) else ''.join(x))
df['doctor_educate_title'] = df['doctor_educate_title'].apply(lambda x:  x if pd.isnull(x) else ''.join(x))
df['hospital'] = df['hospital'].apply(lambda x:  ','.join(x))
df['department'] = df['department'].apply(lambda x:  ','.join(x))
df['major'] = df['major'].apply(lambda x:  ','.join(x)).replace(';','。')
df['profile'] = df['profile'].apply(lambda x:  ','.join(x)).replace(';','。')

df.to_csv('doctor_data.csv', sep=';')
print(df.columns)
print(df)