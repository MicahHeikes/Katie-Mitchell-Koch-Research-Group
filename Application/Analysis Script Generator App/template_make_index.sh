#!/bin/bash

i=1 j=1 
for k in `seq 0 200 100000` 

do

First_frame="$k"
Last_frame="$(($k+200))"

Index_file="index$((i++)).ndx"
Output_file="res_water$((j++)).ndx"


	gmx make_ndx -f ../../../grofile -o $Output_file -n index.ndx $Index_file <<EOF

q

EOF


rm -rf *#     

done
