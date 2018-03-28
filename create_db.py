import csv
import json
import pandas as pd
import sys, getopt, pprint
from pymongo import MongoClient

connection = MongoClient()

#CSV to JSON Conversion
csvfile = open('2_labels.csv', 'r')
reader = csv.DictReader( csvfile )
db = connection.arjuna
db.image_info.drop()
header= [ "", "latitude", "longitude", "image", "cluster", "type", "tags", "Regional Lang", "Translated Lang"]

for each in reader:
    row={}
    for field in header:
        row[field] = each[field]

    db.image_info.insert(row)

print(db.image_info.find())
