# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 10:06:22 2020

@author: Freya Allery
"""

import matplotlib.pyplot as plt
from operator import truediv
import numpy as np
import pandas as pd

df = pd.read_csv('CDD July 2018.csv')

#reading in load data calculated in excel
load = df.kWh

time = ([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23])

plt.plot(time,load)
plt.ylabel('Energy Demand (kWh)')
plt.xlabel('Time of Day')
#labelling times of day
plt.xticks(np.arange(0,24,step = 3),('00:00','03:00','06:00','09:00','12:00','15:00','18:00','21:00','24:00'))
plt.grid()
#setting axis limits
plt.xlim(0,23)
plt.ylim(0,900)