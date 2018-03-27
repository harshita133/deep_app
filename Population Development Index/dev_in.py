import numpy as np

def dev_in(features):
    m = features.shape[0]
    n = features.shape[1]
    
    
    
    w = np.random.seed-(n)
    h = np.zeros(m)
    
    
    for i in range(m):
        for j in range(n):
            if(j==0) :
                h[i] += w[j] * np.log(features[i,j])
            
            elif((j>0) or (j<n-1)):
                h[i] += w[j] * np.log(features[i,j])
            
            else :
                h[i] += w[j] * np.exp(-features[i,j])
    

            
    dev_ind = 1 / (1 + np.exp(-h))
    
    return dev_ind,h
