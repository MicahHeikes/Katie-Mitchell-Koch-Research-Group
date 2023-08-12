#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Read the xvg file and extract the data
filename = 'average_dipcorr.xvg'

with open(filename, 'r') as file:
    lines = file.readlines()

data_start = False
x_data = []
y_data = []

for line in lines:
    if line.startswith('@TYPE'):
        data_start = True
    elif data_start and not line.startswith('@'):
        values = line.split()
        try:
            x_value = float(values[0])
            y_value = float(values[1])
            x_data.append(x_value)
            y_data.append(y_value)
        except ValueError:
            continue

# Define the exponential function with 4 parameters
def exponential_function(x, a, b, c, d):
    return a * np.exp(-x / b) + c * np.exp(-x / d)

# Perform the curve fitting
popt, pcov = curve_fit(exponential_function, x_data, y_data)

# Extract the optimized parameters
a_opt, b_opt, c_opt, d_opt = popt

# Generate the fitted curve
x_fit = np.linspace(min(x_data), max(x_data), 100)
y_fit = exponential_function(x_fit, a_opt, b_opt, c_opt, d_opt)

# Plot the original data and the fitted curve
plt.plot(x_data, y_data, 'bo', label='Data')
plt.plot(x_fit, y_fit, 'r-', label='Fitted Curve')
plt.xlabel('Time (ps)')
plt.ylabel('C(t)')
plt.legend()

# Save the plot to a file
plt.savefig('plot.png')

# Save the optimized parameters to a file
with open('optimized_parameters.txt', 'w') as file:
    file.write(f"Optimized parameters: a = {a_opt:.3f}, b = {b_opt:.3f}, c = {c_opt:.3f}, d = {d_opt:.3f}")
