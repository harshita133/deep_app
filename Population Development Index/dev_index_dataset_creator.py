import numpy as np
import pandas as pd
from dev_in import dev_in

data  = pd.read_csv("population_census_data.csv")

m = data.shape[0]
n = data.shape[1]
bias = np.ones(m)
bias = pd.DataFrame(bias)

X = pd.concat([bias,data],axis=1)

m = X.shape[0]
n = X.shape[1]

X_arr = X.values
d_i,hyp = dev_in(X_arr)

d_i = pd.DataFrame(d_i,columns = ['Development Index'])

data = pd.concat([data,d_i],axis=1)

print(data)

data.to_csv('Community Assets Dev Index.csv')


