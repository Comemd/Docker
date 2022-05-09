import pandas as pd # data processing
import numpy as np # working with arrays
import matplotlib.pyplot as plt # visualization
import seaborn as sb # visualization
from termcolor import colored as cl # text customization

from sklearn.model_selection import train_test_split # data split

df = pd.read_csv('House_Data.csv')
df.describe()
df.dropna()
df_drop.astype({'MasVnrArea' : 'int64'}).dtypes

x_var = df_drop[[col for col in df_drop.columns.drop('Id').drop('SalePrice')]].values
y_var = df_drop['SalePrice'].values
    
x_train, x_test, y_train, y_test = train_test_split(x_var, y_var,test_size=0.20)