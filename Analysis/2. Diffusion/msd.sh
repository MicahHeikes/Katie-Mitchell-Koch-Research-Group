#!/bin/bash

# This bash script is the one that gives us mean square
# displacement and produces a graphical representation.
# In this case we are looking at each index file which 
# represents the water present in 200ps intervals, and 
# and following the waters for 200ps.  Group "16" is the 
# index file we created listing each water molecule within
# 6 A of the residues we are looking at.


i=1 j=1 
for k in `seq 0 200 50000` 

do

First_frame="$k"
Last_frame="$(($k+200))"

Index_file="index$((i++)).ndx"
Output_file="msd$((j++)).xvg"

group="18"

	gmx msd -f ../../../../mdnoPBC.xtc -s ../../../../md.gro -o $Output_file  -b $First_frame -e $Last_frame -n $Index_file -beginfit 10 -endfit 75 <<EOF

$group

EOF


rm -rf *#     

done
