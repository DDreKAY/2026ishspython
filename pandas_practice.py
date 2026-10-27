from multiprocessing.reduction import duplicate

import seaborn as sns
import pandas as pd
import numpy as np

df = sns.load_dataset('penguins')
df.info()
print(df.isna().sum())
print(df.head(5))
print(df.groupby('species')[['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g']].mean())
df=df.groupby('species')[['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g']].apply(lambda x: x.fillna(x.mean()))
print(df.head(5))