# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
import sys

assert sys.version_info >= (3, 7)
#
#
#
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

np.random.seed(42)

plt.rc('font', size=12)
plt.rc('axes', labelsize=14, titlesize=14)
plt.rc('legend', fontsize=12)
plt.rc('xtick', labelsize=10)
plt.rc('ytick', labelsize=10)
#
#
#
#
data_source_raw = "/datasets/heart.csv"
data_source_result = pd.read_csv(data_source_raw)
x_values = data_source_result["Age"].values
y_values = data_source_result["RestingBP"].values

lifesat.plot(kind='scatter', grid=True, x="GDP per capita (USD)", y="Life satisfaction")
#
#
#
#
plt.show()
#
#
#
