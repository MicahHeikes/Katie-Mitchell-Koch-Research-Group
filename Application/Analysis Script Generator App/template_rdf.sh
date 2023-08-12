#!/bin/bash


mkdir resi
cd resi

gmx rdf -f ../../../xtcfile -s ../../../grofile -seltype res_com -n index.ndx -bin 0.05 <<EOF
18
13
EOF
cd ../