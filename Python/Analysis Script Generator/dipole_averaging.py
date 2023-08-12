#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import glob

# Get a list of all xvg files starting with 'dipcorr'
file_list = glob.glob('dipcorr*.xvg')

# Initialize variables for averaging
num_files = len(file_list)
averaged_data = []

# Loop through each file and accumulate the data
for file_name in file_list:
    with open(file_name, 'r') as file:
        data = []
        for line in file:
            if line.startswith('@') or line.startswith('#'):
                continue
            if line.startswith('@TYPE'):
                break
            values = line.split()
            if len(values) < 2:
                continue
            value = float(values[1])
            if len(data) == 0:
                data = [value]
            else:
                data.append(value)

        if len(averaged_data) == 0:
            averaged_data = data
        else:
            for i in range(len(data)):
                averaged_data[i] += data[i]

# Average the accumulated data
averaged_data = [value / num_files for value in averaged_data]

# Write the averaged data to a file
with open('average_dipcorr.xvg', 'w') as file:
    file.write('# Averaged Dipole Autocorrelation Function\n')
    file.write('@    xaxis  label "Time (ps)"\n')
    file.write('@    yaxis  label "C(t)"\n')
    file.write('@TYPE xy\n')
    with open(file_list[0], 'r') as ref_file:
        for line in ref_file:
            if line.startswith('@') or line.startswith('#'):
                file.write(line)
            if line.startswith('@TYPE'):
                break
        for i, value in enumerate(averaged_data):
            file.write('{:.3f} {:.5f}\n'.format(i * 0.2, value))








