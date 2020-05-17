# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 10:19:37 2020

@author: Freya Allery, developed from https://bit.ly/2zQXiID
"""

import time
import matplotlib.pyplot as plt
from pid_to_run import PID


class WaterBoiler:
    

    def __init__(self):
        self.water_temp = 30

    def update(self, boiler_power, dt):
        if boiler_power > 0:
            # heating from boiler
            self.water_temp += 1 * boiler_power * dt

        # heat dissipation
        self.water_temp -= 0.02 * dt
        return self.water_temp


if __name__ == '__main__':
    boiler = WaterBoiler()
    water_temp = boiler.water_temp

    pid = PID(6, 0.03, 0.1, setpoint=water_temp)
    pid.output_limits = (0, 60)

    start_time = time.time()
    last_time = start_time

    # Storing values for plotting
    setpoint, y, x = [], [], []

    while time.time() - start_time < 10:
        current_time = time.time()
        dt = current_time - last_time

        power = pid(water_temp)
        water_temp = boiler.update(power, dt)

        x += [current_time - start_time]
        y += [water_temp]
        setpoint += [pid.setpoint]

        if current_time - start_time > 1:
            pid.setpoint = 60

        last_time = current_time

# Plotting the data
    plt.plot(x, y, label='$T_{measured}$')
    plt.plot(x, setpoint, label='$T_{setting}$')
    plt.xlabel('Time (h)')
    plt.ylabel('Temperature(°C)')
    # Setting x axis
    plt.xlim(0,10)
    plt.grid()
    plt.legend()
    plt.show()
    