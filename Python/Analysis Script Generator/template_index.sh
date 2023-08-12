#!/bin/bash

# This script reads the details.txt file we made line 
# by line and creates an index file listing the assigned 
# molecule we want to analyze (water in our case)

i=1
file="details.txt"

while read line
do

Index_file="index$((i++)).ndx"

gmx make_ndx -f ../../../grofile -o $Index_file <<EOF
r $line
q
EOF
 
rm -rf *#

done < details.txt
