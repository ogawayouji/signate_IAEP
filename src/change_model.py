import pandas as pd
import os
import matplotlib.pyplot as plt


DATA_DIR = './db'
data_file = os.path.join(DATA_DIR, 'data.csv')
data = pd.read_csv(data_file)

# pd.get_dummies(data)

# np.log(カラム名)