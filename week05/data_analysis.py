import pandas as pd
import numpy as np

import pandas as pd

df = pd.read_csv(r"C:\2026ishspython\week05\data_analysis_adv\datasets\bike_rentals\bike_rentals.csv")
df = df.set_index('datetime')
#print(df.head(25))

print(df.filter(like='00:00:00', axis=0))
print(df.filter(items=['weather','count']))
print(df.filter(regex='w.e'))