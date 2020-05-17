# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 10:27:33 2020

@author: Freya Allery
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('HDD Jan 2018.csv') # reading in csv file

To = df.temp # selecting the air temp
Tb = df['base temp'] # selecting the base temp

time = ([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])

plt.fill_between(time,To,Tb,color="orange", # The fill color
                        alpha=0.2)          # Transparency of the fill)
plt.plot(time, To,color = "blue", label = "air temperature")
plt.plot(time, Tb,color = "red", label = "heating base temperature")


#plotting the graph
plt.ylabel('Temperature (°C)')
plt.xlabel('Time of Day')
# labelling times of day
plt.xticks(np.arange(0,24,step = 3),('00:00','03:00','06:00','09:00','12:00','15:00','18:00','21:00','24:00'))
plt.grid()
plt.legend(loc="center right")
#setting x limit
plt.xlim(0,23)

