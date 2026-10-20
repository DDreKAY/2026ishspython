import numpy as np
import pandas as pd

df = pd.read_csv('datasets/bookings/Bookings.csv')
print(df.info())
print(df.head(3))
print(df.tail(3))

print(df['Review'].value_counts())