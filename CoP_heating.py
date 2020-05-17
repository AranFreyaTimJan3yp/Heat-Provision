# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 09:06:39 2020

@author: Freya Allery
"""

import numpy as np 
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# outdoor temps
Tc = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
# possible base temps
Th1 = np.array([17.5,17.5,17.5,17.5,17.5,17.5,17.5,17.5,17.5,17.5,17.5,17.5,17.5,17.5,17.5])
Th2 = np.array([18.5,18.5,18.5,18.5,18.5,18.5,18.5,18.5,18.5,18.5,18.5,18.5,18.5,18.5,18.5])
Th3 = np.array([19.5,19.5,19.5,19.5,19.5,19.5,19.5,19.5,19.5,19.5,19.5,19.5,19.5,19.5,19.5])

# Create function that adds 273 to make temps be in Kelvin
add_273 = lambda i: i + 273

# Create vectorized function
vectorized_add_273 = np.vectorize(add_273)

# Apply function to all elements to make temps in K
Tc_K = vectorized_add_273(Tc)
Th1_K = vectorized_add_273(Th1)
Th2_K = vectorized_add_273(Th2)
Th3_K = vectorized_add_273(Th3)


T_diff = (abs(Th1_K-Tc_K))
T_diff2 = (abs(Th2_K-Tc_K))
T_diff3 = (abs(Th3_K-Tc_K))
print(T_diff2)

CoP1 = 0.1*Th1_K/(T_diff)
CoP2 = 0.1*Th2_K/(T_diff2)
CoP3 = 0.1*Th3_K/(T_diff3)
print(CoP2)

plt.plot(Tc,CoP1,label="base temp 17.5℃")
plt.plot(Tc,CoP2,label = "base temp 18.5℃")
plt.plot(Tc,CoP3,label = "base temp 19.5℃")
plt.legend(loc="upper left")
plt.ylabel('Heating COP')
plt.xlabel('Outside Temperature (℃)')
#plt.title('CoP for Heating')
plt.grid()
plt.xlim(0,14)