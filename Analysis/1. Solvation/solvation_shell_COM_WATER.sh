#!/bin/bash

# This script calls our index.ndx file and selects all water within 6 Angstroms.  It does this in 200ps increments.

cd 1-12

gmx select -f ../../../../mdnoPBC.xtc -s ../../../../md.gro -select '"Water" group SOL and within 0.6 of group "1-12-sidechain"' -seltype res_com -n index.ndx -dt 200 -oi <<EOF
EOF

cd ..

cd 13-18

gmx select -f ../../../../mdnoPBC.xtc -s ../../../../md.gro -select '"Water" group SOL and within 0.6 of group "13-18-sidechain"' -seltype res_com -n index.ndx -dt 200 -oi <<EOF
EOF

cd ..

cd 20-32

gmx select -f ../../../../mdnoPBC.xtc -s ../../../../md.gro -select '"Water" group SOL and within 0.6 of group "20-32-sidechain"' -seltype res_com -n index.ndx -dt 200 -oi <<EOF
EOF

cd ..

cd 44-57

gmx select -f ../../../../mdnoPBC.xtc -s ../../../../md.gro -select '"Water" group SOL and within 0.6 of group "44-57-sidechain"' -seltype res_com -n index.ndx -dt 200 -oi <<EOF
EOF

cd ..

cd 58-66

gmx select -f ../../../../mdnoPBC.xtc -s ../../../../md.gro -select '"Water" group SOL and within 0.6 of group "58-66-sidechain"' -seltype res_com -n index.ndx -dt 200 -oi <<EOF
EOF

cd ..

cd 67-75

gmx select -f ../../../../mdnoPBC.xtc -s ../../../../md.gro -select '"Water" group SOL and within 0.6 of group "67-75-sidechain"' -seltype res_com -n index.ndx -dt 200 -oi <<EOF
EOF

cd ..

cd 76-93

gmx select -f ../../../../mdnoPBC.xtc -s ../../../../md.gro -select '"Water" group SOL and within 0.6 of group "76-93sidechain"' -seltype res_com -n index.ndx -dt 200 -oi <<EOF
EOF

cd ..

cd 94-98

gmx select -f ../../../../mdnoPBC.xtc -s ../../../../md.gro -select '"Water" group SOL and within 0.6 of group "94-98-sidechain"' -seltype res_com -n index.ndx -dt 200 -oi <<EOF
EOF

cd ..

cd 118-124

gmx select -f ../../../../mdnoPBC.xtc -s ../../../../md.gro -select '"Water" group SOL and within 0.6 of group "118-124-sidechain"' -seltype res_com -n index.ndx -dt 200 -oi <<EOF
EOF

cd ..

cd 142-146

gmx select -f ../../../../mdnoPBC.xtc -s ../../../../md.gro -select '"Water" group SOL and within 0.6 of group "142-146-sidechain"' -seltype res_com -n index.ndx -dt 200 -oi <<EOF
EOF

cd ..

cd 147-151

gmx select -f ../../../../mdnoPBC.xtc -s ../../../../md.gro -select '"Water" group SOL and within 0.6 of group "147-151-sidechain"' -seltype res_com -n index.ndx -dt 200 -oi <<EOF
EOF

cd ..

cd 162-169

gmx select -f ../../../../mdnoPBC.xtc -s ../../../../md.gro -select '"Water" group SOL and within 0.6 of group "162-169-sidechain"' -seltype res_com -n index.ndx -dt 200 -oi <<EOF
EOF

cd ..

cd 170-178

gmx select -f ../../../../mdnoPBC.xtc -s ../../../../md.gro -select '"Water" group SOL and within 0.6 of group "170-178-sidechain"' -seltype res_com -n index.ndx -dt 200 -oi <<EOF
EOF

cd ..

cd 184-211

gmx select -f ../../../../mdnoPBC.xtc -s ../../../../md.gro -select '"Water" group SOL and within 0.6 of group "184-211-sidechain"' -seltype res_com -n index.ndx -dt 200 -oi <<EOF
EOF

cd ..

cd 217-225

gmx select -f ../../../../mdnoPBC.xtc -s ../../../../md.gro -select '"Water" group SOL and within 0.6 of group "217-225-sidechain"' -seltype res_com -n index.ndx -dt 200 -oi <<EOF
EOF

cd ..

cd 225-242

gmx select -f ../../../../mdnoPBC.xtc -s ../../../../md.gro -select '"Water" group SOL and within 0.6 of group "225-242-sidechain"' -seltype res_com -n index.ndx -dt 200 -oi <<EOF
EOF

cd ..

cd 243-245

gmx select -f ../../../../mdnoPBC.xtc -s ../../../../md.gro -select '"Water" group SOL and within 0.6 of group "243-245-sidechain"' -seltype res_com -n index.ndx -dt 200 -oi <<EOF
EOF

cd ..

cd 246-248

gmx select -f ../../../../mdnoPBC.xtc -s ../../../../md.gro -select '"Water" group SOL and within 0.6 of group "246-248-sidechain"' -seltype res_com -n index.ndx -dt 200 -oi <<EOF
EOF

cd ..

cd 249-253

gmx select -f ../../../../mdnoPBC.xtc -s ../../../../md.gro -select '"Water" group SOL and within 0.6 of group "249-253-sidechain"' -seltype res_com -n index.ndx -dt 200 -oi <<EOF
EOF

cd ..

cd 254-262

gmx select -f ../../../../mdnoPBC.xtc -s ../../../../md.gro -select '"Water" group SOL and within 0.6 of group "254-262-sidechain"' -seltype res_com -n index.ndx -dt 200 -oi <<EOF
EOF

cd ..

cd 264-267

gmx select -f ../../../../mdnoPBC.xtc -s ../../../../md.gro -select '"Water" group SOL and within 0.6 of group "264-267-sidechain"' -seltype res_com -n index.ndx -dt 200 -oi <<EOF
EOF

cd ..

cd 268-287

gmx select -f ../../../../mdnoPBC.xtc -s ../../../../md.gro -select '"Water" group SOL and within 0.6 of group "268-287-sidechain"' -seltype res_com -n index.ndx -dt 200 -oi <<EOF
EOF

cd ..

cd 309-317

gmx select -f ../../../../mdnoPBC.xtc -s ../../../../md.gro -select '"Water" group SOL and within 0.6 of group "309-317-sidechain"' -seltype res_com -n index.ndx -dt 200 -oi <<EOF
EOF

cd ..