#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 00:32:33 2018
@author: rishab
"""

import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

def Ai(interface_lang, label_):

	count = CountVectorizer()

	info = [interface_lang]

	bag = count.fit_transform(info)

	analyze = count.build_analyzer()

	arr = analyze(info[0])

	arr2 = np.unique(arr)

	arr3 = np.array(label_)

	arr2 = np.concatenate((arr2 , arr3) , axis = 0)

	edu_tags = ['education' , 'school','university','class']
	medical_tags = ['hospital','health','dispensary','clinic','faculty','surgery','nursing','home','emergency']
	chemist_tags = ['chemist','medical','pharmacy','store']
	water_supply_tags = ['water','supply']
	env_tags = ['forest','river','wildlife','sanctuary','park']
	public_service_tags = ['panchayat','office','union','vidhan','system','rural','authority','development','raj']
	power_supply_tags = ['power','electricity','light']
	gas_supply_tags = ['gas','gasoline','lpg','indane','hp']
	filling_stations_tags = ['petrol','diesel','gasoline','cng','petroleum','hp','Indian','oil']
	transport_tags = ['transport','railway','airport','bus','roadways','train']
	awareness_tags = ['scheme','aware','yojna','plan','development']

	(edu , medical , chemist , water_supply , env , public_service , power , gas , filling , transport , awarness )= (0,0,0,0,0,0,0,0,0,0,0)

	find = []
	aware = []

	for i in edu_tags:
	    if i in arr2:
	        find.append([i,'edu_tag'])
	        edu +=1
	for i in medical_tags:
	    if i in arr2:
	        find.append([i,'medical_tag'])
	        medical +=1
	for i in chemist_tags:
	    if i in arr2:
	        find.append([i,'chemist_tags'])
	        chemist +=1
	for i in water_supply_tags:
	    if i in arr2:
	        find.append([i,'water_suply_tags'])
	        water_supply +=1
	for i in env_tags:
	    if i in arr2:
	        find.append([i,'env_tags'])
	        env+=1
	for i in public_service_tags:
	    if i in arr2:
	        find.append([i,'admin_tags'])
	        public_service +=1
	for i in power_supply_tags:
	    if i in arr2:
	        find.append([i,'power_supply_tags'])
	        power +=1
	for i in gas_supply_tags:
	    if i in arr2:
	        find.append([i,'gas_supply_tags'])
	        gas +=1
	for i in filling_stations_tags:
	    if i in arr2:
	        find.append([i,'filling_stations_tags'])
	        filling +=1
	for i in transport_tags:
	    if i in arr2:
	        find.append([i,'transport_tags'])
	        transport +=1
	for i in awareness_tags:
	    if i in arr2:
	        aware.append([i,'awareness_tags'])
	        awarness +=1

	certain_tag = {'Educational_body':edu , 'Medical_body':medical , 'Pharmacy':chemist , 'Water_supply_body':water_supply , 'Environment_management':env , 'public_service_body':public_service , 'Power / Energy Office':power , 'LPG , Natural Gas station':gas , 'Fuel / Filling Station':filling , 'Transportational Asset':transport , 'awarness':awarness}

	type_ = max(certain_tag, key=certain_tag.get)

	# print(type_)

	return (find , aware , type_ , certain_tag , awarness)

