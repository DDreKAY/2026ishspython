import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

df=pd.read_csv("./data_analysis_adv/datasets/Uber/Uber.csv")

df['START_DATE*'] = pd.to_datetime(df['START_DATE*'], errors='coerce')
df['END_DATE*'] = pd.to_datetime(df['END_DATE*'], errors='coerce')

df = df.sort_values(['START_DATE*','END_DATE*'])

df = df.drop(1155)

df['DURATION*'] = (df['END_DATE*'] - df['START_DATE*']).dt.total_seconds() / 60 # total time
df=df.dropna()

slope,bias,rvalue,_,_ = linregress(df['START_DATE*'],df['END_DATE*'])
fig, ax = plt.subplots()
sns.regplot(x='MILES*', y='DURATION*', data=df, ax=ax,
            line_kws={f'label':f'y={slope}x+{bias}, R^2={rvalue**2}'})
'''plt.legend()
plt.show()
'''

# 특성 공학(Feature Engineering) 중 특성 추출:새로운 열을 만들어내는 것

df=pd.read_csv("./data_analysis_adv/datasets/German_credit/German_credit.csv")
ages=[10,20,30,40,50,60,70,80]
print(pd.cut(df['Age'],bins=ages, right=False).reset_index().groupby('Age').size())

# 적당히 수 나눠서 히스토그램 만들기
print(pd.qcut(df['Age'], q=8,duplicates='drop').reset_index().groupby('Age').size())
