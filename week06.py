import numpy as np
import pandas as pd

df = pd.read_csv('./datasets/bookings/bookings.csv')

df['Total_Review'] = df['Total_Review'].map(lambda x: str(x).replace('external','').strip())
df['Total_Review'] = df['Total_Review'].map(lambda x: str(x).replace('review','').strip())
df['Total_Review'] = df['Total_Review'].map(lambda x: str(x).replace(',',''))
df['Total_Review'] = df['Total_Review'].astype('float')
df['Rating']=df['Rating'].ffill()
df['Total_Review']=df['Rating'].fillna(df['Rating'].mean())

quantile = [0, 0.2, 0.4, 0.6, 0.8, 1]

for idx in quantile:
    q = df['Total_Review'].quantile(idx, interpolation='higher')
    print(f"quantile {idx} is {q}")