import numpy as np
import pandas as pd
import seaborn as sns

df = sns.load_dataset('penguins')
'''print(df.head(5))
print(df.tail(5))
print(df.describe())
df.info()'''

print(df.value_counts())
bl = int(input('Enter bill length: '))
species = input('Enter species: ')
print(df.query('bill_length_mm >= @bl and species == @species'))

# query 메서드 조건문의 문자열 메서드 사용
df.query('island.str.contains("oe")', engine='python')

df.query('species.str.endswith("e")', engine='python')

'''# query 메서드를 이용한 부등호 필터링
df.query('bill_length_mm > 55')

# 위 코드와 동일한 결과를 얻음
df[df['bill_length_mm'] > 55]

# 위 코드와 동일한 결과를 얻음
df.loc[df['bill_length_mm'] > 55]'''