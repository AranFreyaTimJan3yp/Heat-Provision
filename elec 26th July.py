# -*- coding: utf-8 -*-
"""
Created on Wed May 13 22:20:37 2020

@author: Freya Allery
"""

import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np

import pandas as pd

df = pd.read_csv('CDD July 2018.csv')

#COP for heating in morning
Tc1 = df.Tc
Th1 = df['base temp 2']

Tc1[ Tc1==0 ] = np.nan # not plotting data where temp is within base temps


# Create function that adds 273
add_273 = lambda i: i + 273

# Create vectorized function
vectorized_add_273 = np.vectorize(add_273)

# Apply function to all elements 
Tc1_K = vectorized_add_273(Tc1) #K
Th1_K = vectorized_add_273(Th1) #K

T_diff1 = (abs(Th1_K-Tc1_K))

COP1 = (Th1_K/(T_diff1))*0.1

# limiting COP to 4.85 to ensure realistic values are given
COP1[COP1 > 4.85] = 4.85

#COP for cooling in day
Tc2 = df['base temp']
Th2 = df.Th

Th2[ Th2==0 ] = np.nan  # not plotting data where temp is within base temps


# Create function that adds 273
add_273 = lambda i: i + 273

# Create vectorized function
vectorized_add_273 = np.vectorize(add_273)

# Apply function to all elements 
Tc2_K = vectorized_add_273(Tc2) #K
Th2_K = vectorized_add_273(Th2) #K

T_diff2 = (abs(Th2_K-Tc2_K)) # temp difference

# factor of 0.1 to account for losses
COP2 = 0.1*Tc2_K/(T_diff2)


# limiting COP to 4.85 to ensure realistic values are given
COP2[COP2 > 4.85] = 4.85

df = pd.read_csv('CDD July 2018.csv')


# selecting load calculated in excel from csv file
load = df.kWh

# calculating electricity values
elec_h = load/COP1
elec_c = load/COP2

time = ([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])

#plotting data

plt.plot(time,elec_h, color = 'orange', label = 'electricity demand for heating')
plt.plot(time,elec_c, color = 'blue', label = 'electricity demand for cooling')
         

plt.ylabel('Electricity Demand (kWh)')
plt.xlabel('Time of Day')
plt.xticks(np.arange(0,24,step = 3),('00:00','03:00','06:00','09:00','12:00','15:00','18:00','21:00','24:00'))
plt.grid()
plt.legend(loc="upper left")
plt.xlim(0,23)
plt.ylim(0,300)
