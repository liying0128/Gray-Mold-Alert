import pandas as pd
import numpy as np
min_lx=165
range_lx=10212
min_temp=8.05
range_temp=35.86
min_humidity=36.2
range_humidity=60.19

temp_center_norm=0.2215
humi_center_norm=0.8626
lx_center_norm=0.1905

dist=[]

data=pd.read_excel(datafile)
data_norm=np.zeros((len(data),4))
for i in range(len(data.iloc[:,0])):
    data_norm.iat[i,0]=(data.iat[i,0]min_temp)/range_temp

for i in range(len(data.iloc[:,1])):
    data_norm.iat[i,1]=(data.iat[i,1]min_humidity)/range_humidity
    
for i in range(len(data.iloc[:,2])):
    data_norm.iat[i,2]=(data.iat[i,2]min_lx)/range_lx

for i in range(len(data.iloc[:,2])):
    data_norm.iat[i,3]=((data.iat[i,0]-temp_center_norm)**2+(data.iat[i,1]-humi_center_norm)**2+(data.iat[i,2]-lx_center_norm)**2)**0.5

for i in range (len(data.iloc[:,5])):
    dist.append(i)

if np.mean(dist[(len(dist)-5:)])<0.3:
    print('High possibility of gray mold')
if np.mean(dist[(len(dist)-5:)])<0.3:
    print('Very high possibility of gray mold')