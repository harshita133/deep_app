#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 00:32:33 2018
@author: rishab
"""

from __future__ import print_function, division
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
import numpy as np
import pandas as pd
from ai import Ai
from core import Core
from cluster_analysis import Cluster_analysis

dict_ref = {'Educational_body':60 , 'Medical_body':3 , 'Pharmacy':10 , 'Water_supply_body':12 , 'Environment_management':1 , 'public_service_body':12 , 'Power / Energy Office':3 , 'LPG , Natural Gas station':10 , 'Fuel / Filling Station':40 , 'Transportational Asset':50 , 'awarness':5}
population = 10000

def sigmoid(x):
    sigmoid_score = (1 / float(1 + np.exp(- x)))
    return sigmoid_score

def equation(dict_):
	DI = 0
	for tag in dict_:
		DI += (dict_ref[tag]*(sigmoid((dict_[tag]/population)*(100000/dict_ref[tag]))))
	return DI

def Cluster(dataset_name , n_classes):

	# n_classes = 2

	X = pd.read_csv('dataset.csv',sep=',')

	X = X.dropna(axis = 0).reset_index()

	name = X[['image']]

	arr = X['image'].as_matrix()

	type_csv = []
	tags_csv = []
	extracted_tag = []
	translated_tag = []

	for i in arr:
		(text, extracted_lang, label_) = Core(i, lan)
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

	result.to_csv('{}_labels.csv'.format(n_classes))

	arr = []

	for i in range(n_classes):
		count = Cluster_analysis(i)
		DI = equation(count)
		print(DI)
		df = pd.read_csv('{}_labels.csv'.format(n_classes) , sep = ",")
		X = df[df['cluster'] == i]
		l = len(X)
		arr.append([round(DI,3)]*l)
	arr_new = np.concatenate((arr[0],arr[1]), axis=0)
	df_new = df.sort_values('cluster',ascending=True).reset_index()
	df2 = pd.DataFrame(data = arr_new , columns = ['Dev_Index'])
	result = pd.concat([df_new , df2] , axis = 1)
	result = result.loc[:, ~result.columns.str.contains('^Unnamed')]
	result = result.loc[:, ~result.columns.str.contains('^index')]
	result.to_csv('{}_labels.csv'.format(n_classes))
	print(result)
	return result
