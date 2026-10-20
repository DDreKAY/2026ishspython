import numpy as np
import pandas as pd

df = pd.read_csv('datasets/bookings/Bookings.csv')
'''print(df.info())
print(df.head(3))
print(df.tail(3))

print(df['Review'].value_counts()'''

df.loc[df['Review'] == "Superb 9.0", "Review"] = "Superb "
df.loc[df['Review'] == "Superb ", "Review"] = "Superb"
df.loc[df['Review'] == "Exceptional 10", "Review"] = "Exceptional "
df.loc[df['Review'] == "Exceptional ", "Review"] = "Exceptional"
#print(df['Review'].value_counts())

df['Total_Review'] = df['Total_Review'].map(lambda x: str(x).replace('external','').strip())
df['Total_Review'] = df['Total_Review'].map(lambda x: str(x).replace('review','').strip())
df['Total_Review'] = df['Total_Review'].map(lambda x: str(x).replace(',',''))
df['Total_Review'] = df['Total_Review'].astype('float')
df['Total_Review'] = df['Total_Review'].fillna(df['Total_Review'].median())

#print(df.info())

#print(df['Total_Review'].unique())

index = df[df['Rating'].isna()].tail().index
print(df[df['Rating'].isna()].index)
df['Rating'] = df['Rating'].fillna(df['Rating'].mean())

s=pd.Series([1,np.nan,np.nan,2,np.nan,3])
print(s)
s=s.ffill()
print(s)