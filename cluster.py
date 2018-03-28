#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 00:32:33 2018
@author: rishab
"""

from __future__ import print_function
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
import numpy as np
import pandas as pd
from ai import Ai
from core import Core

# from sklearn.decomposition import PCA
# import matplotlib.pyplot as plt
# import matplotlib.cm as cm

def Cluster(dataset_name , n_classes):

	# n_classes = 2

	X = pd.read_csv('test_dataset.csv',sep=',')

	X = X.dropna(axis = 0).reset_index()

	name = X[['image']]

	arr = X['image'].as_matrix()

	type_csv = []
	tags_csv = []
	extracted_tag = []
	translated_tag = []

	for i in arr:
		(text, extracted_lang, label_) = Core(i)
		(find , aware , type_ , certain_tag , awarness) = Ai(extracted_lang , label_)
		type_csv.append(type_)
		tags_csv.append(str(label_))
		extracted_tag.append(text)
		translated_tag.append(extracted_lang)

	X = X[['latitude','longitude']]

	clusterer = KMeans(n_clusters= n_classes, random_state=1 , max_iter = 10000)
	cluster_labels = clusterer.fit_predict(X)

	df = pd.DataFrame(data = X )
	df2 = pd.DataFrame(data = cluster_labels , columns = ['cluster'])
	df3 = pd.DataFrame(data = type_csv , columns = ['type'])
	df4 = pd.DataFrame(data = tags_csv , columns = ['tags'])
	df5 = pd.DataFrame(data = extracted_tag , columns = ['Regional Lang'])
	df6 = pd.DataFrame(data = translated_tag , columns = ['Translated Lang'])

	result = pd.concat([ name , df , df2 , df3 , df4 , df5 , df6 ] , axis = 1)

	print(result)

	result.to_csv('{}_labels.csv'.format(n_classes))

	return result