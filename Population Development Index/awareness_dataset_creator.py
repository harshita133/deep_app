import numpy as np
import csv
import pandas as pd

X = {
     'scheme' : np.random.randint(0,5,40),
     'aware' : np.random.randint(0,5,40),
     'yojna' : np.random.randint(0,5,40),
     'movement' : np.random.randint(0,5,40),
     'plan' : np.random.randint(0,5,40),
     'development' : np.random.randint(0,5,40),
     'freedom' : np.random.randint(0,5,40),
     'Be the change' : np.random.randint(0,5,40),
     'human rights' : np.random.randint(0,5,40),
     'innovation' : np.random.randint(0,5,40),
     'innovate' : np.random.randint(0,5,40),
     'ban' : np.random.randint(0,5,40),
     'independence' : np.random.randint(0,5,40),
     'yoga' : np.random.randint(0,5,40),
     'change the world' : np.random.randint(0,5,40),
     'human rights' : np.random.randint(0,5,40)     
     }

#X.to_csv('awareness_dataset.csv')
data1 = []
data2 = []

for i in X:
    data1.append(X[i])
    data2.append(i)



#with open('awareness_training_dataset.csv','w') as f:
#    
#    fieldnames = X.keys
#    w = csv.DictWriter(f,fieldnames=fieldnames)
#    w.writeheader()
#    w.writerows(X.items())

#s = pd.Series(X,index=X.keys())
#s = pd.Series(X)
    
    
    
j = pd.DataFrame(data1 = np.transpose(np.array(data)) , columns = np.array(data2))
print(j)
j.to_csv('awareness_dataset.csv')