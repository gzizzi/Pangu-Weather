#grib pressure level files into numpy array

import pygrib
import numpy as np
from numpy import *


# Create an empty list to store the 3D NumPy arrays
array_list = []

array_shape = (5, 721, 1440)  

# Number of arrays you want to create
num_arrays = 14  

# Create and append 3D NumPy arrays to the list with indexed names
for i in range(num_arrays):
    # Create a sample 3D NumPy array (replace this with your own data)
    arr = np.empty(array_shape, dtype=float32)  # Replace with your own array creation logic
    # Append the NumPy array to the list with a name that includes the index 'i'
    array_list.append(arr)


# Open the GRIB file
grbs = pygrib.open('/work3/zizzi/soclimpact_medcordex/Pangu-Weather/input_upper_15_09_2020_12.grib')

#d_var and d_plev dictionaries not used
#d_var={1:'Z_' ,2:'Q_', 3:'T_',4:'U_',5:'V_'}
#d_plev={1:"1000",2:'925',3:'850',4:'700',5:'600',6:'500',7:'400',8:'300',9:'250',10:'200',11:'150',12:'100',13:'50',}    
d_cost={1:60,2:55,3:50,4:45,5:40,6:35,7:30,8:25,9:20,10:15,11:10,12:5,13:0} 


for i, arr in enumerate(array_list[1:], start=1):   # loop in [1-14[ 
    
    Z_data=0;Q_data=0;T_data=0;U_data=0;V_data=0;
    
    for j in range(1,6):
       I=d_cost.get(i)+j
       if j == 1:
          Z_data = grbs[I].values
          #print("Z mess:", grbs[I])
       if j == 2:
          Q_data = grbs[I].values
          #print("Q mess:", grbs[I])
       if j == 3:
          T_data = grbs[I].values
          #print("T mess:", grbs[I])
       if j == 4:
          U_data = grbs[I].values
          #print("U mess:", grbs[I])
       if j == 5:
          V_data = grbs[I].values
          #print("V mess:", grbs[I])
#    print("----------------------------------------------")

    array_list[i] = stack((Z_data, Q_data, T_data, U_data, V_data), axis=0)    
  

stacked_array = np.stack([array_list[i] for i in range(1, 14)], axis=1)    
#print(stacked_array)    
#stacked_array_without_masked = stacked_array.filled(np.nan)
# Close the GRIB file
grbs.close()

unmasked_array = stacked_array.data

# Save the NumPy array as a .npy file
#np.save('/work3/zizzi/soclimpact_medcordex/Pangu-Weather/download_upper_27_09_2018.npy', stacked_array_without_masked)
np.save('/work3/zizzi/soclimpact_medcordex/Pangu-Weather/input_upper_15_09_2020_12.npy', unmasked_array)

#come posso identificare tali valori?
#come spiegare la loro presenza?
#sistema codice
#grib_surf2numpy.py
#grib_upper2numpy.py
#esempi suggeriti da Leone

