#!/usr/bin/env python
# coding: utf-8

# In[4]:


# open both the input and output files
with open('Optimized_Coefficients.txt', 'r') as infile, open('reorientation_times.txt', 'w') as outfile:
    # iterate over each line in the input file
    for line in infile:
        # remove the prefix and split the line into parts by comma
        parts = line.replace("Optimized parameters:", "").split(',')
        # check if the line has the expected number of parts
        if len(parts) == 4:
            try:
                # extract the values of a, b, c, and d from the parts
                a = float(parts[0].split('=')[1])
                b = float(parts[1].split('=')[1])
                c = float(parts[2].split('=')[1])
                d = float(parts[3].split('=')[1])

                # perform the operation (a*b) + (c*d)
                result = (a * b) + (c * d)

                # write the result to the output file
                outfile.write(f'{result}\n')
            except ValueError:
                print(f"Couldn't parse line: {line}")
        else:
            print(f"Line doesn't match expected format: {line}")


# In[ ]:




