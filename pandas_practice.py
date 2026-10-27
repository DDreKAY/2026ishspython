from multiprocessing.reduction import duplicate

import seaborn as sns
import pandas as pd

# Titanic.csv
df = sns.load_dataset("titanic")
print(df.head())
print(df.describe())
print(df.info())

df = df.drop(columns=["alive"])
df = df.drop(columns=["embarked"])
df = df.drop(columns=["class"])
print(df.info())
