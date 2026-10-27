from multiprocessing.reduction import duplicate

import seaborn as sns
import pandas as pd
import numpy as np

# Titanic.csv
df = sns.load_dataset("titanic")
#print(df.head())
#print(df.describe())
#print(df.info())
print(df["survived"].value_counts())
print(df["alive"].value_counts())
df1 = df.drop(columns=["alive", "embarked", "class"])
'''df = df.drop(columns=["alive"])
df = df.drop(columns=["embarked"])
df = df.drop(columns=["class"]'''

#print(df1.groupby(['sex','pclass'])["survived"].mean())
print(df1.groupby(['sex','pclass'])[["survived","age"]].agg({'survived':'mean','age':'median'}))

print(df1[['sibsp','parch','who','alone']].value_counts())

def get_IQR(data):
    _3rd = data.quantile(.75)
    _1st = data.quantile(.25)
    return (_3rd - _1st) * 1.5
print(df1.groupby(['sex','pclass'])['age'].apply(get_IQR))