import pandas as pd

s = pd.Series([0, 0, 1, 1, 0, 1, 1, 1, 1, 0])
sc = s.cumsum()
print(s.mul(sc))
print(s.mul(sc).diff())
print(s.mul(sc).diff().where(lambda x : x < 0)) # where: 조건문 빼고 다 NaN로
print(s.mul(sc).diff().where(lambda x : x < 0).ffill()) # forward fill, bfill -> backward fill
print(s.mul(sc).diff().where(lambda x : x < 0).ffill().add(sc, fill_value=0).max())
