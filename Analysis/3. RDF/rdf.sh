#!/bin/bash

# This script uses our previously made index file which contains our solvent accessible residues, and with that as our reference structure 
# we will look at the distance of every water molecule in relation to that. It will give us a graph of the population of water around the 
# selected residues of interest. 

cd 1-12
gmx rdf -f ../../../mdnoPBC.xtc -s ../../../md.gro -seltype res_com -n index.ndx -bin 0.05 <<EOF
18
13
EOF
cd ..

cd 13-18
gmx rdf -f ../../../mdnoPBC.xtc -s ../../../md.gro -seltype res_com -n index.ndx -bin 0.05 <<EOF
18
13
EOF
cd ..

cd 20-32
gmx rdf -f ../../../mdnoPBC.xtc -s ../../../md.gro -seltype res_com -n index.ndx -bin 0.05 <<EOF
18
13
EOF
cd ..

cd 44-57
gmx rdf -f ../../../mdnoPBC.xtc -s ../../../md.gro -seltype res_com -n index.ndx -bin 0.05 <<EOF
18
13
EOF
cd ..

cd 58-66
gmx rdf -f ../../../mdnoPBC.xtc -s ../../../md.gro -seltype res_com -n index.ndx -bin 0.05 <<EOF
18
13
EOF
cd ..

cd 67-75
gmx rdf -f ../../../mdnoPBC.xtc -s ../../../md.gro -seltype res_com -n index.ndx -bin 0.05 <<EOF
18
13
EOF
cd ..

cd 76-93
gmx rdf -f ../../../mdnoPBC.xtc -s ../../../md.gro -seltype res_com -n index.ndx -bin 0.05 <<EOF
18
13
EOF
cd ..

cd 94-98
gmx rdf -f ../../../mdnoPBC.xtc -s ../../../md.gro -seltype res_com -n index.ndx -bin 0.05 <<EOF
18
13
EOF
cd ..

cd 118-124
gmx rdf -f ../../../mdnoPBC.xtc -s ../../../md.gro -seltype res_com -n index.ndx -bin 0.05 <<EOF
18
13
EOF
cd ..

cd 142-146
gmx rdf -f ../../../mdnoPBC.xtc -s ../../../md.gro -seltype res_com -n index.ndx -bin 0.05 <<EOF
18
13
EOF
cd ..

cd 147-151
gmx rdf -f ../../../mdnoPBC.xtc -s ../../../md.gro -seltype res_com -n index.ndx -bin 0.05 <<EOF
18
13
EOF
cd ..

cd 162-169
gmx rdf -f ../../../mdnoPBC.xtc -s ../../../md.gro -seltype res_com -n index.ndx -bin 0.05 <<EOF
18
13
EOF
cd ..

cd 170-178
gmx rdf -f ../../../mdnoPBC.xtc -s ../../../md.gro -seltype res_com -n index.ndx -bin 0.05 <<EOF
18
13
EOF
cd ..

cd 184-211
gmx rdf -f ../../../mdnoPBC.xtc -s ../../../md.gro -seltype res_com -n index.ndx -bin 0.05 <<EOF
18
13
EOF
cd ..

cd 217-225
gmx rdf -f ../../../mdnoPBC.xtc -s ../../../md.gro -seltype res_com -n index.ndx -bin 0.05 <<EOF
18
13
EOF
cd ..

cd 225-242
gmx rdf -f ../../../mdnoPBC.xtc -s ../../../md.gro -seltype res_com -n index.ndx -bin 0.05 <<EOF
18
13
EOF
cd ..

cd 243-245
gmx rdf -f ../../../mdnoPBC.xtc -s ../../../md.gro -seltype res_com -n index.ndx -bin 0.05 <<EOF
18
13
EOF
cd ..

cd 246-248
gmx rdf -f ../../../mdnoPBC.xtc -s ../../../md.gro -seltype res_com -n index.ndx -bin 0.05 <<EOF
18
13
EOF
cd ..

cd 249-253
gmx rdf -f ../../../mdnoPBC.xtc -s ../../../md.gro -seltype res_com -n index.ndx -bin 0.05 <<EOF
18
13
EOF
cd ..

cd 254-262
gmx rdf -f ../../../mdnoPBC.xtc -s ../../../md.gro -seltype res_com -n index.ndx -bin 0.05 <<EOF
18
13
EOF
cd ..

cd 264-267
gmx rdf -f ../../../mdnoPBC.xtc -s ../../../md.gro -seltype res_com -n index.ndx -bin 0.05 <<EOF
18
13
EOF
cd ..

cd 268-287
gmx rdf -f ../../../mdnoPBC.xtc -s ../../../md.gro -seltype res_com -n index.ndx -bin 0.05 <<EOF
18
13
EOF
cd ..

cd 309-317
gmx rdf -f ../../../mdnoPBC.xtc -s ../../../md.gro -seltype res_com -n index.ndx -bin 0.05 <<EOF
18
13
EOF
cd ..
