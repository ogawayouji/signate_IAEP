import pandas as pd
import os
DATA_DIR = './db'
data_file = os.path.join(DATA_DIR, 'data.csv')
data = pd.read_csv(data_file)
# data.head()
# data.info()
# data.shape (行, 列)
# data.drop(columns='column名')

# 欠損値
# data.isnull().sum()
# data.dropna()
# data.fillna()