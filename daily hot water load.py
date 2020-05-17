# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 15:27:54 2020

@author: Freya Allery
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('seasonal water consumption.csv')

load = df.load

time = ([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])

plt.plot(time,load)


plt.xticks(np.arange(0,24,step = 3),('00:00','03:00','06:00','09:00','12:00','15:00','18:00','21:00','24:00'))
#plt.legend(loc="lower right")
plt.grid()
plt.xlabel('Time of Day')
plt.ylabel('Energy Demand (kWh)')
# Setting x axis
plt.xlim(0,23)
# Setting y axis
plt.ylim(0,1200)