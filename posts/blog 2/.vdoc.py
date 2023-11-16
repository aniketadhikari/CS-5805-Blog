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
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#
#
#
data = pd.read_csv("../../datasets/pokemon.csv", sep=",")
data['total_attack'] = data['attack'] + data['sp_attack']
data['total_defense'] = data['defense'] + data['sp_defense']
data
#
#
#
