import csv
import numpy as np
import pandas as pd

dataset = pd.read_csv("Hospital_directory.csv")

x = dataset[ ['Location_Coordinates','Hospital_Name','Specialties','Facilities'] ]
index = []
specialties_tag = np.array([''])
facilities_tag = np.array([''])
specialties_count = dict()
facilities_count = dict()

for i in range(len(x)):
	#print(x['Specialties'][i])
	if x['Specialties'][i] == '0' or x['Facilities'][i] == '0':
		continue
	elif ( x['Specialties'][i] != [] or x['Facilities'][i] != [] ):
		
		index.append(i)
		breakage = ["\n","and","\\n"]
		Sp_t = str(x['Specialties'][i])
		Fc_t = str(x['Facilities'][i])

		for b in breakage:
			if b in Sp_t:
				Sp_t = Sp_t.replace(b,',')
			if b in Fc_t:
				Fc_t = Fc_t.replace(b,',') 
		
		sp_tags = Sp_t.split(',')
		fc_tags = Fc_t.split(',')
		#print(sp_tags)
		#print(specialties_tag)
		for j,s in enumerate(sp_tags):
			sp_tags[j] = s.strip()
			if sp_tags[j] == "":
				continue
			match_mask = np.where(specialties_tag == sp_tags[j])
			if np.all(match_mask):
				specialties_count.update({sp_tags[j]:1})
			else:
				specialties_count[sp_tags[j]] = specialties_count[sp_tags[j]] + 1

		for j,f in enumerate(fc_tags):
			fc_tags[j] = f.strip()
			if fc_tags[j] == "":
				continue
			match_mask = np.where(facilities_tag == fc_tags[j])
			if np.all(match_mask):
				facilities_count.update({fc_tags[j]:1})
			else:
				facilities_count[fc_tags[j]] = facilities_count[fc_tags[j]] + 1
				
		specialties_tag = np.unique(np.append(specialties_tag,sp_tags))
		facilities_tag = np.unique(np.append(facilities_tag,fc_tags))	
	else:
		pass

print("Different specialties our country provides:")
print(specialties_tag)
print("Different facilities our hospitals provide:")
print(facilities_tag)
print("Occurances of specialties:")
print(specialties_count)
print("Occurances of facilities:")
print(facilities_count)
print(len(specialties_tag),len(specialties_count))

# two tables:
# table 1: specialties, hospitals serving those specialties and their count; facilities, hospitals serving those facilities and their count
#data = pd.DataFrame({'Location_Latitude':})

