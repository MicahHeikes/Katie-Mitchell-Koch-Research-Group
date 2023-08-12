#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from scipy.stats import linregress

def read_xvg(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    data = []
    for line in lines:
        if not line.startswith(('@', '#')):
            try:
                # each value is separated by a space or tab, convert each to float
                values = [float(x) for x in line.split()]
                data.append(values)
            except ValueError:
                print(f"Skipping line: {line}")
    
    return np.array(data)

def calculate_diffusion_coefficient(msd, time_data):
    slope, intercept, r_value, p_value, std_err = linregress(time_data, msd)
    diffusion_coefficient = slope / 6
    return diffusion_coefficient

def main():
    output_filename = "Diff_Linear_Regression.txt"
    with open(output_filename, 'w') as output_file:
        for i in range(1, 501):
            filename = f"msd{i}.xvg"
            displacement_data = read_xvg(filename)

            # select the time frame between 10 and 70
            indices = np.where((displacement_data[:, 0] >= 10) & (displacement_data[:, 0] <= 70))
            selected_data = displacement_data[indices]

            time_data = selected_data[:, 0]
            msd = selected_data[:, 1]

            diffusion_coefficient = calculate_diffusion_coefficient(msd, time_data)

            # Convert diffusion coefficient to cm^2/s
            diffusion_coefficient_cm2_per_s = diffusion_coefficient / 100

            # Write diffusion coefficient to output file
            output_file.write(f"The diffusion coefficient for {filename} is: {diffusion_coefficient_cm2_per_s} cm^2/s\n")

if __name__ == "__main__":
    main()


# In[ ]:




