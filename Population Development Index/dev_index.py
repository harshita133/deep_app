import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt 

df = pd.read_csv("");

X = df.iloc[:,1:9]
Y = df.iloc[:,9]

pca = PCA(n_components=2)
T = pca.fit_transform(X)
print(T)










