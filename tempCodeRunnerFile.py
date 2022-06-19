from tkinter import font
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 8})
from datetime import datetime
from keras.models import Sequential
from keras.layers import Dense, LSTM, Dropout, GRU
from keras.layers import *
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split
from keras.callbacks import EarlyStopping
from keras.optimizers import Adam, SGD


headers = ["Date","Open","High","Low","Close","Adj","Volume"]
df = pd.read_csv('data.csv', names=headers)
df = df.sort_values('Date').reset_index(drop=True)
print(df['Date'][-predict.shape[0]:].values)