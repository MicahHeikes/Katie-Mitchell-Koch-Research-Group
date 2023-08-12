#!/bin/bash

cd resi

gmx select -f ../../../xtcfile -s ../../../grofile -select '"Water" group SOL and within 0.6 of group "resi-sidechain"' -seltype res_com -n index.ndx -dt 200 -oi <<EOF
EOF

cd ..
