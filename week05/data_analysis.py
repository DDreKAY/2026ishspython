import pandas as pd
import numpy as np

import pandas as pd

df = pd.read_csv(r"C:\2026ishspython\week05\data_analysis_adv\datasets\bike_rentals\bike_rentals.csv")
df.info()

# select_dtypes 메서드를 사용하여 int형 변수만 선택
df.select_dtypes(include='int')

# select_dtypes 메서드를 사용하여 int형 변수만 제외하여 선택
df.select_dtypes(exclude='int')