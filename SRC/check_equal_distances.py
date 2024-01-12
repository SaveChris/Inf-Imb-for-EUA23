import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from dadapy import Data
from dadapy import DataSets as ds
from sklearn.preprocessing import StandardScaler
from utils_zero_dist_imbalance import _get_imbalance_from_d1_to_d2, _get_average_imbalance_from_d1_to_d2
from scipy.spatial.distance import pdist, squareform

df = pd.read_excel('Dataset_eua_IMv4.3.xlsx')

eua = df['eua_last']

X = df.iloc[:,3:]

# get numpy array from pandas dataframe
X = X.values
y = eua.values
y = y.reshape(-1,1)

labels = df.columns[3:]

scaler = StandardScaler()
X = scaler.fit_transform(X)
y = scaler.fit_transform(y)

# split data at 1782 
X_3 = X[1782:,:]#4
y_3 = y[1782:,:]#4

X_4 = X[:1782, :]#3
y_4 = y[:1782, :]#3

### for debugging purposes
#X_3 = np.random.normal(0, 1, (100, 1))
#y_3 = np.random.normal(0, 1, (100, 1))

d_y_3 = Data(y_3 , maxk=y_3.shape[0]-1)
d_y_3.compute_distances()

d_3 = Data(X_3, maxk=X_3.shape[0]-1)
d_3.compute_distances()

d_y3_dist_matrix = squareform(pdist(y_3, 'euclidean'))

imbalance = _get_imbalance_from_d1_to_d2(d_3, d_y_3)
imbalance_average = _get_average_imbalance_from_d1_to_d2(d_3, d_y3_dist_matrix)

print(imbalance)
print(imbalance_average)


inf_imb_X_to_y = []
inf_imb_X_to_y_average = []


for i in range(X_3.shape[1]):
    print(i)
    d_3_i = Data(X_3[:, [i]], maxk=X_3.shape[0]-1)
    d_3_i.compute_distances()
    inf_imb_X_to_y.append(_get_imbalance_from_d1_to_d2(d_3_i, d_y_3))

    inf_imb_X_to_y_average.append(_get_average_imbalance_from_d1_to_d2(d_3_i, d_y3_dist_matrix))


# sort the imbalances according to inf_imb_X_to_y_average
sort_idx = np.argsort(inf_imb_X_to_y_average)
inf_imb_X_to_y_average = np.array(inf_imb_X_to_y_average)[sort_idx]
inf_imb_X_to_y = np.array(inf_imb_X_to_y)[sort_idx]
labels = labels[sort_idx]

plt.figure(figsize=(5, 5))
plt.plot(inf_imb_X_to_y_average)
plt.plot(inf_imb_X_to_y)
plt.xticks(np.arange(len(labels)), labels, rotation=90)
plt.xlabel('Imbalance')
plt.title('Phase 3')
plt.tight_layout()
plt.savefig('inf_imb_X_to_y.png')
plt.show()
