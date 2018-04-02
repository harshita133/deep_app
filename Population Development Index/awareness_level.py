import numpy as np 
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier

awrns = pd.read_csv("awareness_dataset.csv")
    
m = awrns.shape[0]
n = awrns.shape[1]

clustering = KMeans(n_clusters=3,random_state=10)
clustering.fit(awrns)

clusters = pd.DataFrame(clustering.labels_)


awrns_data = pd.concat([awrns,clusters],axis=1)
#awrns_data.to_csv('awareness_dataset1.csv')

X = awrns.as_matrix()
y = clusters.as_matrix()

classifier = RandomForestClassifier(max_depth=None,random_state=0)

classifier.fit(X,y)

from sklearn.externals import joblib 
joblib.dump(classifier,"rf_40.pkl")

print(classifier.predict([[3,3,2,4,4,1,0,1,0,3,0,1,0,3,3]]))




