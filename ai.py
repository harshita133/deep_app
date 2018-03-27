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
	admin_tags = ['panchayat','office','union','vidhan','system','rural','authority','development','raj']
	power_supply_tags = ['power','electricity','light']
	gas_supply_tags = ['gas','gasoline','lpg','indane','hp']
	filling_stations_tags = ['petrol','diesel','gasoline','cng','petroleum','hp','Indian','oil']
	transport_tags = ['transport','railway','airport','bus','roadways','train']
	awareness_tags = ['scheme','aware','yojna','plan','development']

	find = []
	aware = []
	for i in edu_tags:
	    if i in arr2:
	        find.append([i,'edu_tag'])
	for i in medical_tags:
	    if i in arr2:
	        find.append([i,'medical_tag'])
	for i in chemist_tags:
	    if i in arr2:
	        find.append([i,'chemist_tags'])
	for i in water_supply_tags:
	    if i in arr2:
	        find.append([i,'water_suply_tags'])
	for i in env_tags:
	    if i in arr2:
	        find.append([i,'env_tags'])
	for i in admin_tags:
	    if i in arr2:
	        find.append([i,'admin_tags'])
	for i in power_supply_tags:
	    if i in arr2:
	        find.append([i,'power_supply_tags'])
	for i in gas_supply_tags:
	    if i in arr2:
	        find.append([i,'gas_supply_tags'])
	for i in filling_stations_tags:
	    if i in arr2:
	        find.append([i,'filling_stations_tags'])
	for i in transport_tags:
	    if i in arr2:
	        find.append([i,'transport_tags'])

	for i in awareness_tags:
	    if i in arr2:
	        aware.append([i,'awareness_tags'])

	return (find , aware)