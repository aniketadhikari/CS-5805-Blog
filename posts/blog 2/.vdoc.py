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
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#
#
#
#
#
data = pd.read_csv("../../datasets/pokemon.csv", sep=",")
data
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
data['Total Attack'] = data['attack'] + data['sp_attack']
data['Total Defense'] = data['defense'] + data['sp_defense']
#
#
#
#
#
x_val = 'Total Attack'
y_val = 'Total Defense'
values = [x_val, y_val]
X = data[values] 
#
#
#
#
#
kmeans = KMeans(n_clusters=3)
#
#
#
#
kmeans.fit(X)
#
#
#
#
labels = kmeans.labels_
colormap = np.array(['red', 'green', 'blue'])
#
#
#
#
#
plt.scatter(X['Total Attack'], X['Total Defense'], c=colormap[labels])
plt.title('Pokemon Attack and Defense Clusters')
plt.xlabel('Total Attack')
plt.ylabel('Total Defense')

plt.show()
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
import pandas as pd
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt
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
customer_data = pd.read_csv('../../datasets/Customers.csv')
#
#
#
#
#
selected_features = ['Age', 'Annual Income ($)', 'Work Experience']
#
#
#
#
#
customer_features = customer_data[selected_features]
customer_features = (customer_features - customer_features.mean()) / customer_features.std()
#
#
#
#
#
#
#
num_clusters = 3
gmm = GaussianMixture(n_components=num_clusters)
gmm.fit(customer_features)
cluster_labels = gmm.predict(customer_features)
customer_data['Cluster'] = cluster_labels
#
#
#
#
#
plt.scatter(x=customer_data["Age"], y=customer_data["Annual Income ($)"], c=cluster_labels, cmap="Set2")
plt.xlabel("Age")
plt.ylabel("Income")
plt.suptitle('Customer Segmentation using GMM')
plt.show()
#
#
#
