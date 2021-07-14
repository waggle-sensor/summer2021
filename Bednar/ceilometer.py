from  netCDF4 import Dataset

filename = 'sgpceilC1b120191121000000.nc'

nc = Dataset(filename, 'r')
print(nc.variables)


firstcloud = nc.variables['first_cbh'][:]
secondcloud = nc.variables['second_cbh'][:]
thirdcloud = nc.variables['third_cbh'][:]

timeoff = nc.variables['timeoffset'][:]

for j in range(0,5401):
 print( firstcloud[j],secondcloud[j],thirdcloud[j],timeoff[j])
nc.close()
