#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

def block_average(values, num_blocks):
    block_size = len(values) // num_blocks
    averaged_values = []

    with open("Block_Averaging_20Blocks.txt", "a") as output_file:
        output_file.write("Block Averaging Results\n")
        output_file.write("---------------------------\n")

        for i in range(num_blocks):
            block_start = i * block_size
            block_end = (i + 1) * block_size
            block = values[block_start:block_end]
            block_average = np.mean(block)
            averaged_values.append(block_average)
            output_file.write("Block {} Average: {}\n".format(i + 1, block_average))

    return averaged_values


def read_values_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        values = []
        for line in lines:
            if line.startswith("The diffusion coefficient"):
                value_str = line.split(":")[1].strip()
                value = float(value_str.split()[0])
                values.append(value)

    return values


# Example usage
file_path = 'Diff_Linear_Regression.txt'  # Update with your file path
values = read_values_from_file(file_path)
num_blocks = 20  # Set the total number of blocks to 20

averaged_values = block_average(values, num_blocks)
block_average_mean = np.mean(averaged_values)
block_average_std = np.std(averaged_values)
block_average_variance = np.var(averaged_values)

with open("Block_Averaging_20Blocks.txt", "a") as output_file:
    output_file.write("\n")
    output_file.write("Average of Block-Averaged Values: {}\n".format(block_average_mean))
    output_file.write("Standard Deviation of Block-Averaged Values: {}\n".format(block_average_std))
    output_file.write("Variance of Block-Averaged Values: {}\n".format(block_average_variance))

print("Block averaging results have been saved in 'Block_Averaging_20Blocks.txt'.")


# In[ ]:




