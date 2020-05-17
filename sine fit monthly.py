# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 12:51:06 2020

@author: Freya Allery
"""

import numpy as np
from scipy.optimize import leastsq
import pylab as plt
import pandas as pd

df = pd.read_csv('2018 monthly temps.csv')

N = 8760 # number of data points
t = np.linspace(0, 4*np.pi, N)
data = df.temperature # read temperature column

est_mean = np.mean(data)
est_std = 3*np.std(data)/(2**0.5)/(2**0.5)
est_phase = 1.5
est_freq = 1
est_amp = 0.5

# to plot the first estimate
data_est = est_std*np.sin(t+est_phase) + est_mean

# defining the function to optimise to then minimise the difference
# between the actual data and estimated parameters
func = lambda x: x[0]*np.sin(x[1]*t+x[2]) + x[3] - data
amp, freq, phase, mean = leastsq(func, [est_amp, est_freq, est_phase, est_mean])[0]

# fitting the curve using the optimised parameters
data_fit = amp*np.sin(freq*t+phase) + mean


month_t = np.arange(0,max(t),0.1)
data_fit=amp*np.sin(freq*month_t+phase)+mean



plt.plot(t, data, '.', label = 'hourly temperature data')
plt.xlabel('Time in Months')
plt.ylabel('Temperature (°C)')
plt.plot(t, data_est, label='estimate',color = 'green')
plt.plot(month_t, data_fit, label='after fitting', color = 'orange')
# limiting the x axis
plt.xlim(0,12)
plt.legend()
plt.show()


