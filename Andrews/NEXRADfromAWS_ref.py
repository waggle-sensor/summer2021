#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nexradaws
import tempfile
from matplotlib import pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import pyart
from datetime import datetime, timedelta
import numpy as np
import pytz
import pandas as pd

import warnings
warnings.filterwarnings('ignore')


# In[2]:


# Central lat/lon of ARM SGP site 
lat_sgp = 36.607322
lon_sgp = -97.487643


# In[3]:


# Create temp file, connect to NEXRAD AWS, request files by date & station ID
templocation = tempfile.mkdtemp()
conn = nexradaws.NexradAwsInterface()
#scans = conn.get_avail_scans(2019, 11, 10, 'KVNX')
scans = conn.get_avail_scans(2019, 8, 22, 'KVNX')


# In[4]:


# Download selected volume scans
num_scans = scans[100:105]
localfiles = conn.download(num_scans, templocation)

dt = []
ref = []
count = 0

# Loop through downloaded scans
for scan in localfiles.iter_success():
        
    # Pyart doesn't like or can't seem to read in the MDM files so I'm ignoring them
    if 'MDM' in str(scan): 
        count+=1
    
    else:
        print('Reading in: '+scan.filename)
    
        # Read in the selected volume scans (that don't end in MDM)
        radar = pyart.io.read(localfiles.success[count].filepath)
        
        # Grab the times of the scans for plotting
        t = scan.scan_time # UTC
        times = dt.append(t)
        
        # Loop through each sweep
        for x in radar.iter_slice():

            # Get lat/lon/alt of all the gates in the sweep
            lat = radar.gate_latitude['data'][x]
            lon = radar.gate_longitude['data'][x]
            alt = radar.gate_altitude['data'][x] # meters

            # Calculate lat/lon of the gate closest to ARM SGP site
            dist = np.sqrt((lat - lat_sgp)**2 + (lon - lon_sgp)**2)
            min_idx = np.where(dist == dist.min())
            lat_lcn = lat[min_idx]
            lon_lcn = lon[min_idx]
            height = alt[min_idx]

            # Get reflectivity value at that lat/lon
            reflectivity = radar.fields['reflectivity']['data'][min_idx[0], min_idx[1]]
            
            #gt_hgt.append(height)
            ref.append(reflectivity)
            print('Lat,lon,hgt,ref of the gate closest to SGP site:', lat_lcn, lon_lcn, height, reflectivity)
        
        count+=1    

#print(ref)
#print(dt)


# In[5]:


# Plot 
fig = plt.figure(figsize=[10,10])

ax = plt.axes(projection=ccrs.PlateCarree())

display = pyart.graph.RadarMapDisplay(radar)
display.plot_ppi_map('reflectivity', 0, vmin=-8, vmax=64, ax=ax, embelish=False, colorbar_flag=False)

cbar = plt.colorbar(mappable=display.plots[0], fraction=.1, shrink=.8, label='NEXRAD Z$_e$ (dBZ)')

grid = ax.gridlines(draw_labels=True,
                  linewidth=1, color='gray', alpha=0.5, linestyle='--')

grid.ylabels_right = False
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.STATES)
ax.add_feature(cfeature.LAKES, zorder=0)
#plt.scatter(lon_lcn, lat_lcn, marker='o', color='red', s=15)
plt.scatter(lon_sgp, lat_sgp, marker='*', color='black', s=100)


# In[6]:


#radar.info()


# In[7]:


# Get gate height array for plotting
gt_hgt = []

for y in radar.iter_slice():
    lat = radar.gate_latitude['data'][y]
    lon = radar.gate_longitude['data'][y]
    height = radar.gate_altitude['data'][y] # meters
    dist = np.sqrt((lat - lat_sgp)**2 + (lon - lon_sgp)**2)
    min_idx = np.where(dist == dist.min())
    hgt = height[min_idx]
    gt_hgt.append(hgt)
print(gt_hgt)


# In[8]:


# Trying to figure how to make a time height array with the reflectivity values and plot it
# This is a horrifying, there are clearly better ways
swp1 = ref[::18]

df = pd.DataFrame({'date': dt,
                   'sweep1': swp1})

df['time']= df['date'].dt.time
df = df.set_index(['time'])
df


# In[ ]:




