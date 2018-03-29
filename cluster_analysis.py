import pandas as pd
import numpy as np

def Cluster_analysis(cluster_index):

	X = pd.read_csv('2_labels.csv',sep=',')

	consi = X[X['cluster'] == cluster_index]

	dic = np.unique(consi['type'].as_matrix() , return_counts = True)

	result = {}

	for i,j in zip(dic[0],dic[1]):
		result[i] = j

	return(result)