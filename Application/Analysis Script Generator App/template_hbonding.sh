#!/bin/bash

i=1 j=1 l=1
for k in `seq 0 200 100000` 

do

First_frame="$k"
Last_frame="$(($k+200))"

Index_file="res_water$((i++)).ndx"
Output_file1="numHbonds$((j++)).xvg"
Output_file2="hbac$((l++)).xvg"

 gmx hbond -f ../../../xtcfile -s ../../../tprfile -num $Output_file1 -b $First_frame -e $Last_frame -n $Index_file -P 1 -temp 300 -ac $Output_file2 <<EOF

18
37

EOF


rm -rf *#     

done
