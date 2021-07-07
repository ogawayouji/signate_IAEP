import pandas as pd
import os
import matplotlib.pyplot as plt


DATA_DIR = './db'
data_file = os.path.join(DATA_DIR, 'data.csv')
data = pd.read_csv(data_file)
# from sklearn.model_selection import train_test_split
# train_test_split(説明変数x, 目的変数y, random_state, test_size)
# data[['','']]

# |y| = y.actual - y.pred
# Sy = sum(|y| * |y|)
# mean = Sy/n
# RMSE = sqrt(mean)

# from sklearn.metrics import mean_squared_error as MSE
# MSE = RMSE * RMSE
# MSE(autual, pred)

# from sklearn.linear_model import LinearRegression
# model = LR()
# model.fit(x, y)
# model.predict(X)
# maximum
# minimum
# 対角線 min_value, max_value  min_value, max_value
