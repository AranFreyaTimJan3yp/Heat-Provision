# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 12:23:48 2020

@author: Freya Allery
"""

import matplotlib.dates as mdates
import numpy as np 
import matplotlib.pyplot as plt
import datetime
import csv

# Importing 2014 degree days data 
with open ('CDD 2014.csv',newline='') as csvfile:
    temp_difference = csv.reader(csvfile,delimiter=',')
    
    deltaT = []
    
    line = 0
    for row in temp_difference:
        if line >= 1:
            deltaT.append(float(row[1])) # Selecting the data for 24℃
        line+=1


deltaT = np.array(deltaT)

# Total floor area for housing and science park
A = 720955.4 # m^2


T = deltaT
a = sum(deltaT)
    

# Using 0.01492kWh/m^2 per year from passive house standards to scale data
cooling_energy = 0.01492e-3*A # MWh
# Scaling the cooling energy
b = cooling_energy/a
scaled_cooling_energy=cooling_energy*T/a
#print(a) # sum of degree days

# Generating some random date-time data
numdays = 364
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

# Importing 2018 degree days data 
with open ('CDD 2014.csv',newline='') as csvfile:
    temp_difference = csv.reader(csvfile,delimiter=',')
    
    deltaT = []
    
    line = 0
    for row in temp_difference:
        if line >= 1:
            deltaT.append(float(row[1])) # Selecting the data for 24℃
        line+=1


deltaT = np.array(deltaT)

# Total floor area for housing and science park
A = 720955.4 # m^2


T = deltaT
a = sum(deltaT)

# Using 0.11723kWh/m^2 per year from passive house standards to scale data
cooling_energy = 0.11723e-3*A # MWh
# Scaling the cooling energy
b = cooling_energy/a
scaled_cooling_energy1=cooling_energy*T/a
#print(a) # sum of degree days

# Generating some random date-time data
numdays = 364
base = datetime.datetime(2014,1,1)
date_list1 = [base + datetime.timedelta(days=x) for x in range(0, numdays)]
# Setting the locator
locator = mdates.MonthLocator()  # every month
# Specifying the format (%b gives us Jan, Feb...)
fmt = mdates.DateFormatter('%b')
X = plt.gca().xaxis
X.set_major_locator(locator)
# Specify formatter
X.set_major_formatter(fmt)
X = plt.gca().set_xlim([date_list[0], date_list[-1]])

# Importing 2019 degree days data 
with open ('CDD 2019.csv',newline='') as csvfile:
    temp_difference = csv.reader(csvfile,delimiter=',')
    
    deltaT = []
    
    line = 0
    for row in temp_difference:
        if line >= 1:
            deltaT.append(float(row[1])) # Selecting the data for 24℃
        line+=1


deltaT = np.array(deltaT)

# Total floor area for housing and science park
A = 720955.4 # m^2


T = deltaT
a = sum(deltaT)
    

# Using 0.07165kWh/m^2 per year from passive house standards to scale data
cooling_energy = 0.07165e-3*A # MWh
# Scaling the cooling energy
b = cooling_energy/a
scaled_cooling_energy2=cooling_energy*T/a
#print(a) # sum of degree days

# Generating some random date-time data
numdays = 364
base = datetime.datetime(2014,1,1)
date_list2 = [base + datetime.timedelta(days=x) for x in range(0, numdays)]
# Setting the locator
locator = mdates.MonthLocator()  # every month
# Specifying the format (%b gives us Jan, Feb...)
fmt = mdates.DateFormatter('%b')
X = plt.gca().xaxis
X.set_major_locator(locator)
# Specify formatter
X.set_major_formatter(fmt)
X = plt.gca().set_xlim([date_list[0], date_list[-1]])

# Plotting the graph
plt.plot(date_list, scaled_cooling_energy, linewidth=0.5, label="2014")
plt.plot(date_list1, scaled_cooling_energy1, linewidth=0.5, label="2018")
plt.plot(date_list2, scaled_cooling_energy2, linewidth=0.5, label="2019")

#Labelling the graph
plt.ylabel('Cooling Demand (MWh)')
plt.xlabel('Month')
#plt.title('Cooling Profile')
plt.legend(loc="upper right")
plt.grid()

# Setting the x axis in the month format
locator = mdates.MonthLocator()
plt.gca().xaxis.set_major_locator(locator)
# Setting y limit
plt.ylim(0,14)
