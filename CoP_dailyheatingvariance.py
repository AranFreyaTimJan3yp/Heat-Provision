# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 13:02:29 2020

@author: Freya Allery
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('HDD Jan 2018.csv')

Tc = df.temp # reading in hourly temp
Th = df['base temp'] # reading in base temp

# Create function that adds 273 to convert to Kelvin
add_273 = lambda i: i + 273

# Create vectorized function
vectorized_add_273 = np.vectorize(add_273)

# Apply function to all elements to make temps in K
Tc_K = vectorized_add_273(Tc)
Th_K = vectorized_add_273(Th)

# difference between base temp and outside temo
T_diff = (abs(Th_K-Tc_K))


time = ([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])

# calculating COP using factor of 0.1 to account for losses
CoP1 = 0.1*Th_K/(T_diff)


# plotting data
plt.plot(time,CoP1,color="orange")
plt.ylabel('COP')
plt.xlabel('Time of Day')
# labelling time of day
plt.xticks(np.arange(0,24,step = 3),('00:00','03:00','06:00','09:00','12:00','15:00','18:00','21:00','24:00'))
plt.grid()
plt.xlim(0,23)