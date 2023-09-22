#surface grib files into numpy arrays

import pygrib
import numpy as np
from numpy import *

# Open the GRIB file
grbs = pygrib.open('/work3/zizzi/soclimpact_medcordex/Pangu-Weather/input_surface_15_09_2020_12.grib')

# Choose a specific field/message from the GRIB file

U10_message = grbs[1]
print(U10_message)

V10_message = grbs[2]
print(V10_message)

T2M_message = grbs[3]
print(T2M_message)

MSLP_message = grbs[4]
print(MSLP_message)
#MSLP_data = MSLP_message.values.astype(np.float32)
#print(MSLP_data)

#does not work...(to do)
#for grb in grbs[:4]:
#    print(grb)

# Extract the data as a NumPy array
U10_data = U10_message.values

V10_data = V10_message.values

T2M_data = T2M_message.values

MSLP_data = MSLP_message.values

#a = np.zeros(shape=(4, 721, 1440))
#a = np.copy(U10_data) 

surface=stack((MSLP_data.astype(np.float32), U10_data.astype(np.float32), V10_data.astype(np.float32), T2M_data.astype(np.float32)) , axis=0)
#surface=stack((MSLP_data, U10_data, V10_data, T2M_data) , axis=0)

#print(surface.shape)
#print(surface)

# Close the GRIB file
grbs.close()

# Save the NumPy array as a .npy file
np.save('/work3/zizzi/soclimpact_medcordex/Pangu-Weather/input_surface_15_09_2020_12.npy', surface)
