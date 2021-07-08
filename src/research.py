import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error as MSE
from sklearn.linear_model import LinearRegression as LR

import csv


DATA_DIR = '../db'
train_file = os.path.join(DATA_DIR, 'train.tsv')
test_file = os.path.join(DATA_DIR, 'test.tsv')
# data = pd.read_csv(data_file)
train = pd.read_csv(train_file, sep='\t')
test = pd.read_csv(test_file, sep='\t')
# print(train.isnull().sum())
train.dropna()
# test.dropna()
# print(train.describe())
# print(train.drop(columns='id').describe())
# print(train)
# print(test)
# print(train.info())
# print(train.corr())
# train.replace(?, 'NaN')
# print(train.head(48))

# train.dropna()
train = train[train['horsepower'] != '?']

train['displacement_log'] = np.log(train['displacement'])
y = train['mpg']
# 'horsepower',
# print(train['horsepower'].dtype)
train['horsepower'].astype(np.float64)
train['horsepower_float'] = train['horsepower'].astype(np.float64)
print(train.describe())
print(train.info())

X = train[['cylinders', 'displacement_log', 'horsepower_float', 'weight', 'acceleration', 'model year', 'origin']]
X = pd.get_dummies(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1, test_size=0.2)

model = LR()
model.fit(X_train, y_train)

print(X_train)
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

mse_y_train = MSE(y_train, y_pred_train)
mse_y_test = MSE(y_test, y_pred_test)

rmse_train = np.sqrt(mse_y_train)
rmse_test = np.sqrt(mse_y_test)
print(rmse_train, rmse_test)
# print(y_test)
# print(y_pred_test)

test = test[test['horsepower'] != '?']
test['displacement_log'] = np.log(test['displacement'])
test['horsepower_float'] = test['horsepower'].astype(np.float64)
z = test[['cylinders', 'displacement_log', 'horsepower_float', 'weight', 'acceleration', 'model year', 'origin']]
z = pd.get_dummies(z)
print(z)
z_pred = model.predict(z)
# print(z_pred[0])
# z_pred[0]

with open('result.csv','w') as f:
  writer = csv.writer(f)
  # print(len(z_pred))
  j = 0
  for i in range(len(z_pred)):
    try:
      # print()
      k = test.at[j, 'id']
    except:
      j += 1
      # print()
      k = test.at[j, 'id']
    # print()
    l = z_pred[i]
    writer.writerow([k, l])
    j += 1

