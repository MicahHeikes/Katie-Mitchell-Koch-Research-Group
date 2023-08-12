#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

# Read the xvg file and extract the data
filename = 'average_Hbond.xvg'

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

# Define the exponential function with 5 parameters
def exponential_function(x, a, b, c, d, e):
    return a * np.exp(-b * x) + c * np.exp(-d * x) + e

# Perform the curve fitting
popt, pcov = curve_fit(exponential_function, x_data, y_data)

# Extract the optimized parameters
a_opt, b_opt, c_opt, d_opt, e_opt = popt

# Calculate H-Bond Lifetime
hbond_lifetime = (a_opt * (1/b_opt)) + (c_opt * (1/d_opt))

# Generate the fitted curve
x_fit = np.linspace(min(x_data), max(x_data), 100)
y_fit = exponential_function(x_fit, a_opt, b_opt, c_opt, d_opt, e_opt)

# Compute R-squared
r_squared = r2_score(y_data, exponential_function(np.array(x_data), a_opt, b_opt, c_opt, d_opt, e_opt))

# Plot the original data and the fitted curve, then save the plot to a file
plt.plot(x_data, y_data, 'bo', label='Data')
plt.plot(x_fit, y_fit, 'r-', label='Fitted Curve')
plt.xlabel('Time (ps)')
plt.ylabel('C(t)')
plt.legend()
plt.text(max(x_data)*0.6, max(y_data)*0.8, f'R² = {r_squared:.3f}', fontsize=12)
plt.savefig('plot.png')

# Write the optimized parameters and H-Bond Lifetime to a file
with open('HB-Lifetime.txt', 'w') as file:
    file.write(f"Optimized parameters: a = {a_opt:.3f}, b = {b_opt:.3f}, c = {c_opt:.3f}, d = {d_opt:.3f}, e = {e_opt:.3f}\n")
    file.write(f"H-Bond Lifetime = {hbond_lifetime:.3f}\n")

