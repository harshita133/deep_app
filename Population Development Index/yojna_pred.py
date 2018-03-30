
import numpy as np
import pandas as pd

cluster_assets = {
    "Hospitals" : 0,
    "Education Body" : 1,
    "Power Supply" : 1,
    "Water Supply" : 1,
    "Transport" : 0,
    "Filling Stations" : 1,
    "Nature" : 0,
    "Public Service Offices" : 1,
    "Police Station" : 0,              
    "Ration Shops" : 10,
    "Post Ofice" : 1
}

type(cluster_assets.get("Medical Body"))

med_yoj = np.array(["Jan Aushadhi","Central Government Health Scheme","Integrated Rural Development Program","Pradhan Mantri Bhartiya Jan Aushadhi Kendra(PMBJK)"])

edu_yoj = np.array(["Shiksha Sahayog Yojana","Sarva Shiksha Abhiyan","Saakshar Bharat","Kanya Saaksharta Protsahan Yojna","Kasturba Gandhi Balika Vidhyalaya Yojna"])

water_yoj = np.array(["Soil and Water Conservation under Hill Area Development Programme-Aug 25, 2011"])

env_yoj = np.array(["Tamil Nadu Biodiversity Conservation and Greening Project (TBGP)","National Afforestation Programme","Green India mission","Intensification of Forest Management Scheme"])

trans_yoj = np.array(["Green Urban Transport Scheme(GUTS) - PM Jan Dhan Yojana"])

def yojna_predictor(cluster_assets):

    shortage = np.array([])
    yojnas = np.array([])
    
    if(cluster_assets.get("Hospitals")<1):
    
        shortage = np.append(shortage,"Hospitals")
        yojnas = np.concatenate((yojnas,med_yoj),axis=1)
    
    if(cluster_assets.get("Education Body")<1):
        
        shortage = np.append(shortage,"Education Body")
        yojnas = np.concatenate((yojnas,edu_yoj),axis=1)

    if(cluster_assets.get("Power Supply")<1):
        
        shortage = np.append(shortage,"Power Supply")
#         yojnas = np.append(yojnas,[{power_yoj}])

    if(cluster_assets.get("Water Supply")<1):
        
        shortage = np.append(shortage,"Water Supply")
        yojnas = np.concatenate((yojnas,water_yoj),axis=1)
        
    if(cluster_assets.get("Transport")<1):
        
        shortage = np.append(shortage,"Transport")
        yojnas = np.append((yojnas,trans_yoj),axis=1)
        
    if(cluster_assets.get("Filling Stations")<1):
        
        shortage = np.append(shortage,"Filing Stations")
#         yojnas = np.append(yojnas,yojnas,[{}])
    
    if(cluster_assets.get("Nature")<1):
        
        shortage = np.append(shortage,"Nature")
        yojnas = np.concatenate((yojnas,env_yoj),axis=1)
    
    if(cluster_assets.get("Public Service Offices")<1):
        
        shortage = np.append(shortage,"Publice Service Offices")
#         yojnas = np.append(yojnas,[{}])
    
    if(cluster_assets.get("Police Station")<1):
        
        shortage = np.append(shortage,"Police Station")
#         yojnas = np.append(yojnas,[{}])
    
    if(cluster_assets.get("Ration Shops")<9):
        
        shortage = np.append(shortage,"Ration Shops")
#         yojnas = np.append(yojnas,[{}])
    
    return [shortage,yojnas]

rep_data = yojna_predictor(cluster_assets)

rep_data
