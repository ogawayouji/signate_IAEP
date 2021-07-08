import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
DATA_DIR = '../db'
data_file = os.path.join(DATA_DIR, 'train.tsv')
data = pd.read_csv(data_file)