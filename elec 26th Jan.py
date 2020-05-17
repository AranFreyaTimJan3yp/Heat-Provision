# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 09:10:05 2020

@author: Freya Allery
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('HDD Jan 2018.csv')

Tc = df.temp
Th = df['base temp']

# Create function that adds 273 
add_273 = lambda i: i + 273

# Create vectorized function
vectorized_add_273 = np.vectorize(add_273)

# Apply function to all elements in matrix
Tc_K = vectorized_add_273(Tc)
Th_K = vectorized_add_273(Th)


T_diff = (abs(Th_K-Tc_K)) # temp difference

# factor of 0.1 to account for losses 
CoP1 = 0.1*Th_K/(T_diff)

df = pd.read_csv('HDD Jan 2018.csv')

# importing load calculated in excel
load = df.kWh

time = ([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])

# calculating electricity demand
elec_h = load/CoP1

#plotting data

plt.plot(time,elec_h,color="orange",label = 'electricity demand for heating')
plt.ylabel('Electricity Demand (kWh)')
plt.xlabel('Time of Day')
plt.xticks(np.arange(0,24,step = 3),('00:00','03:00','06:00','09:00','12:00','15:00','18:00','21:00','24:00'))
#plt.title('CoP for Heating, Jan 20th 2020')
plt.grid()
plt.legend()
plt.xlim(0,23)





