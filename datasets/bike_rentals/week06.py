import numpy as np
import pandas as pd

df = pd.read_csv("bike_rentals.csv")

df.rename(mapper={'temp':'temperature','atemp':'apparent_temperature'}, axis='columns', inplace=True)

df.info()