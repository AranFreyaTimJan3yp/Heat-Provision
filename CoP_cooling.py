# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 10:29:52 2020

@author: Freya Allery
"""

import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# outdoor temp
Th = np.array([26,27,28,29,30,31,32,33,34,35])

#possible base temps
Tc1 = np.array([25,25,25,25,25,25,25,25,25,25])
Tc2 = np.array([23,23,23,23,23,23,23,23,23,23])
Tc3 = np.array([24,24,24,24,24,24,24,24,24,24])


# Create function that adds 273 to make temps in Kelvin
add_273 = lambda i: i + 273

# Create vectorized function
vectorized_add_273 = np.vectorize(add_273)

# Apply function to make temps in K
Th_K = vectorized_add_273(Th)
Tc1_K = vectorized_add_273(Tc1)
Tc2_K = vectorized_add_273(Tc2)
Tc3_K = vectorized_add_273(Tc3)


# Difference in base temp and outdoor temp
T_diff = (abs(Th_K-Tc1_K))
T_diff2 = (abs(Th_K-Tc2_K))
T_diff3 = (abs(Th_K-Tc3_K))

# using factor of 0.1 to account for losses from theoretical COP mac
CoP1 = 0.1*((Tc1_K))/(T_diff)
CoP2 = 0.1*((Tc2_K))/(T_diff2)
CoP3 = 0.1*((Tc3_K))/(T_diff3)

# Plotting data
plt.plot(Th,CoP2,label = "base temp 23℃")
plt.plot(Th,CoP3,label = "base temp 24℃")
plt.plot(Th,CoP1,label="base temp 25℃")
plt.legend(loc="upper right")
plt.ylabel('Cooling COP')
plt.xlabel('Outside Temperature (℃)')
plt.grid()
# setting x axis
plt.xlim(26,35)