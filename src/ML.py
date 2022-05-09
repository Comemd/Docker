import pandas as pd # data processing
import numpy as np # working with arrays
import matplotlib.pyplot as plt # visualization
import seaborn as sb # visualization
from termcolor import colored as cl # text customization


from sklearn.linear_model import LinearRegression


ols = LinearRegression()
ols.fit(x_train, y_train)
predicted_ols = ols.predict(x_test)
ols_yhat = y_test