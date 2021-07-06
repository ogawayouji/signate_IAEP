import pandas as pd
import os
import matplotlib.pyplot as plt
DATA_DIR = './db'
data_file = os.path.join(DATA_DIR, 'data.csv')
data = pd.read_csv(data_file)
# data.describe() 
# data["カラム名"]
# <Series>.plot.hist(title="")
# <Series>.value_count()
# <Series>.plot.bar()

# <DataFrame>.corr()

# heat map
import seaborn as sns
sns.heatmap(<DataFrame>)
# plt.scatter(yoko,tate)
# sns.boxplot(yoko,tate,DataFrame)
