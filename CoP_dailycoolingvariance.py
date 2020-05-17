# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 11:28:21 2020

@author: Freya Allery
"""

import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np


import pandas as pd

df = pd.read_csv('CDD July 2018.csv')

#COP for heating in morning
Tc1 = df.Tc #reading in outside temp
Th1 = df['base temp 2'] # reading in base temp

Tc1[ Tc1==0 ] = np.nan # setting nan values to where temp is within base range
print(Tc1)

# Create function that adds 273
add_273 = lambda i: i + 273

# Create vectorized function
vectorized_add_273 = np.vectorize(add_273)

# Apply function to all elements 
Tc1_K = vectorized_add_273(Tc1)
Th1_K = vectorized_add_273(Th1)

# temp difference
T_diff1 = (abs(Th1_K-Tc1_K))

# heating COP with factor 0.1 to account for losses
COP1 = (Th1_K/(T_diff1))*0.1

COP1[COP1 > 4.85] = 4.85

#COP for cooling in day
Tc2 = df['base temp'] # reading in cooling base temp
Th2 = df.Th #reading in outside temp

Th2[ Th2==0 ] = np.nan # setting nan values for when temp is within base range

# Create function that adds 273
add_273 = lambda i: i + 273

# Create vectorized function
vectorized_add_273 = np.vectorize(add_273)

# Apply function to all elements 
Tc2_K = vectorized_add_273(Tc2)
Th2_K = vectorized_add_273(Th2)

T_diff2 = (abs(Th2_K-Tc2_K))

# cooling COP qit factor 0.1 to account for losses
COP2 = 0.1*Tc2_K/(T_diff2)

COP2[COP2 > 4.85] = 4.85


time = ([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])


#plotting data
plt.plot(time,COP1, color = 'orange', label = 'COP for heating')
plt.plot(time,COP2, color = 'blue', label = 'COP for cooling')


plt.ylabel('COP')
plt.xlabel('Time of Day')
plt.xticks(np.arange(0,24,step = 3),('00:00','03:00','06:00','09:00','12:00','15:00','18:00','21:00','24:00'))
plt.grid()
plt.legend(loc="lower left")
plt.xlim(0,23)