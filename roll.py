#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 04:49:28 2018

@author: rishab
"""
import pandas as pd

df = pd.read_csv('test_dataset.csv' , sep=',')

arr = df['image'].as_matrix()
