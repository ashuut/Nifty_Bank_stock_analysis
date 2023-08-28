import math
import pandas as pd
import matplotlib as plt
import pandas_datareader as web
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential  # Corrected import
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
plt.style.use("fivethirtyeight")
df=web.DataReader('^NSEBANK',data_source='yahoo',start='2018-08-26',end='2023-08-24')