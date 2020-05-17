# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 13:20:59 2020

@author: Freya Allery
"""

import numpy as np
from scipy.optimize import leastsq
import pylab as plt
import pandas as pd
import matplotlib.dates as mdates
import datetime

df = pd.read_csv('2018 monthly temps.csv')

N = 8760 # number of data points
t = np.linspace(0, 4*np.pi, N)

data = df.temperature # importing data

est_mean = np.mean(data)
est_std = 3*np.std(data)/(2**0.5)/(2**0.5)
est_phase = 0
est_freq = 1
est_amp = 1

# estimate
data_est = est_std*np.sin(t+est_phase) + est_mean

# function to optimise
func = lambda x: x[0]*np.sin(x[1]*t+x[2]) + x[3] - data
amp, freq, phase, mean = leastsq(func, [est_amp, est_freq, est_phase, est_mean])[0]

# fitting the curve
data_fit = amp*np.sin(freq*t+phase) + mean

fine_t = np.arange(0,max(t),0.0345)
data_fit=amp*np.sin(freq*fine_t+phase)+mean



numdays = 365
base = datetime.datetime(2014,1,1)
date_list = [base + datetime.timedelta(days=x) for x in range(0, numdays)]
# Setting the locator
locator = mdates.MonthLocator()  # every month
# Specifying the format (%b gives us Jan, Feb...)
fmt = mdates.DateFormatter('%b')
X = plt.gca().xaxis
X.set_major_locator(locator)
# Specify formatter
X.set_major_formatter(fmt)
X = plt.gca().set_xlim([date_list[0], date_list[-1]])





plt.plot(t, data, '.')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.plot(date_list, data_fit)

plt.show()
# Setting the x axis in the month format
locator = mdates.MonthLocator()
plt.gca().xaxis.set_major_locator(locator)
# Setting y limit
plt.ylim(0,20)