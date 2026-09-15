import numpy as np
import pandas as pd

array = np.array(
    [
        [100,89,100,95],
        [97,99,91,96],
        [99,97,82,95]
    ]
)

df = pd.DataFrame(array,columns=['Kor','Eng','Math','Cs'],index=[1,2,3])

print(df.iat[2,1])
print(df.at[3,'Eng'])
print(df)
print(df.iloc[1:, 2:])
print(df.loc[2:3,'Math':'Cs'])
print(df.iloc[:,[0,2]])
print(df.loc[:,['Kor','Math']])

print(df.loc[df['Math']>=95,['Eng','Kor','Cs']])