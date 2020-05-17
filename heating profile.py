# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 12:02:33 2020

@author: Freya Allery
"""

import matplotlib.dates as mdates
import numpy as np 
import matplotlib.pyplot as plt
import datetime
import csv

# Importing 2014 degree days data 
with open ('HDD 2014.csv',newline='') as csvfile:
    temp_difference = csv.reader(csvfile,delimiter=',')
    
    deltaT = []
    
    line = 0
    for row in temp_difference:
        if line >= 1:
            deltaT.append(float(row[5])) # Selecting the data for 18.5℃
        line+=1

deltaT = np.array(deltaT)

# Total floor area for housing and science park
A = 720955.4 # m^2
#T = deltaT
a = sum(deltaT)

# Using 14.98508kWh/m^2 per year from passive house standards to scale data
heating_energy = 14.98508e-3*A # MWh
# Scaling the heating energy
b = heating_energy/a
scaled_heating_energy=heating_energy*deltaT/a
#print(a) # sum of degree days


# Generating some random date-time data
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

# Importing 2018 degree days data 
with open ('HDD 2018.csv',newline='') as csvfile:
    temp_difference = csv.reader(csvfile,delimiter=',')
    
    deltaT = []
    
    line = 0
    for row in temp_difference:
        if line >= 1:
            deltaT.append(float(row[1])) # Selecting the data for 18.5℃
        line+=1

deltaT = np.array(deltaT)

# Total floor area for housing and science park
A = 720955.4 # m^2
#T = deltaT
a = sum(deltaT)

# Using 14.88277kWh/m^2 per year from passive house standards to scale data
heating_energy = 14.88277e-3*A # MWh
# Scaling the heating energy
b = heating_energy/a
scaled_heating_energy2=heating_energy*deltaT/a
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


# Importing 2019 degree days data 
with open ('HDD 2019.csv',newline='') as csvfile:
    temp_difference = csv.reader(csvfile,delimiter=',')
    
    deltaT = []
    
    line = 0
    for row in temp_difference:
        if line >= 1:
            deltaT.append(float(row[1])) # Selecting the data for 18.5℃
        line+=1

deltaT = np.array(deltaT)

# Total floor area for housing and science park
A = 720955.4 # m^2
#T = deltaT
a = sum(deltaT)

# Using 14.92863kWh/m^2 per year from passive house standards to scale data
heating_energy = 14.9283e-3*A # MWh
# Scaling the heating energy
b = heating_energy/a
scaled_heating_energy1=heating_energy*deltaT/a
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


# Plotting the graph
plt.plot(date_list, scaled_heating_energy, linewidth=0.5, label = "2014")
plt.plot(date_list2, scaled_heating_energy2, linewidth=0.5, label = "2018")
plt.plot(date_list1, scaled_heating_energy1, linewidth=0.5, label = "2019")
# Labelling the graph
plt.ylabel('Heating Demand (MWh)')
plt.xlabel('Month')
#plt.title('Heating Profile')
plt.legend(loc="upper right")

# Setting the x axis in the month format
locator = mdates.MonthLocator()
plt.gca().xaxis.set_major_locator(locator)
plt.grid()
# Setting the y limit
plt.ylim(0,90)
