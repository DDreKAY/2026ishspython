import pandas as pd

df = pd.read_csv('./data_analysis_adv/datasets/APPL_price/APPL_price.csv')
#print(df['Close'])

s = df['Close']>175
sc=s.cumsum()
#print(df[s][['Close']])
print(s.mul(sc).diff().where(lambda n: n < 0).ffill().add(sc,fill_value=0).max())

print(df[s][['Date','Close']])