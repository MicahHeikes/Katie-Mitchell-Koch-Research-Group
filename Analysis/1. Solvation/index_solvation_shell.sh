#!/bin/bash

# This script creates a folder for each set of solvent accessible residues, and within each folder creates an index.ndx file
# with only those resdiues forus to call upon later.

mkdir 1-12
cd 1-12

gmx make_ndx -f ../../../../nvt_md.gro <<EOF
ri 1-12 & 8
name 18 1-12-sidechain
q
EOF

cd ..

mkdir 13-18
cd 13-18

gmx make_ndx -f ../../../../nvt_md.gro <<EOF
ri 13-18 & 8
name 18 13-18-sidechain
q
EOF

cd ..


mkdir 20-32
cd 20-32

gmx make_ndx -f ../../../../nvt_md.gro <<EOF
ri 20-32 & 8
name 18 20-32-sidechain
q
EOF

cd ..

mkdir 44-57
cd 44-57

gmx make_ndx -f ../../../../nvt_md.gro <<EOF
ri 44-57 & 8
name 18 44-57-sidechain
q
EOF

cd ..

mkdir 58-66
cd 58-66

gmx make_ndx -f ../../../../nvt_md.gro <<EOF
ri 58-66 & 8
name 18 58-66-sidechain
q
EOF

cd ..

mkdir 67-75
cd 67-75

gmx make_ndx -f ../../../../nvt_md.gro <<EOF
ri 67-75 & 8
name 18 67-75-sidechain
q
EOF

cd ..

mkdir 76-93
cd 76-93

gmx make_ndx -f ../../../../nvt_md.gro <<EOF
ri 76-93 & 8
name 18 76-93-sidechain
q
EOF

cd ..

mkdir 94-98
cd 94-98

gmx make_ndx -f ../../../../nvt_md.gro <<EOF
ri 94-98 & 8
name 18 94-98-sidechain
q
EOF

cd ..

mkdir 118-124
cd 118-124

gmx make_ndx -f ../../../../nvt_md.gro <<EOF
ri 118-124 & 8
name 18 118-124-sidechain
q
EOF

cd ..

mkdir 142-146
cd 142-146

gmx make_ndx -f ../../../../nvt_md.gro <<EOF
ri 142-146 & 8
name 18 142-146-sidechain
q
EOF

cd ..

mkdir 147-151
cd 147-151

gmx make_ndx -f ../../../../nvt_md.gro <<EOF
ri 147-151 & 8
name 18 147-151-sidechain
q
EOF

cd ..

mkdir 162-169
cd 162-169

gmx make_ndx -f ../../../../nvt_md.gro <<EOF
ri 162-169 & 8
name 18 162-169-sidechain
q
EOF

cd ..

mkdir 170-178
cd 170-178

gmx make_ndx -f ../../../../nvt_md.gro <<EOF
ri 170-178 & 8
name 18 170-178-sidechain
q
EOF

cd ..

mkdir 184-211
cd 184-211

gmx make_ndx -f ../../../../nvt_md.gro <<EOF
ri 184-211 & 8
name 18 184-211-sidechain
q
EOF

cd ..

mkdir 217-225
cd 217-225

gmx make_ndx -f ../../../../nvt_md.gro <<EOF
ri 217-225 & 8
name 18 217-225-sidechain
q
EOF

cd ..

mkdir 225-242
cd 225-242

gmx make_ndx -f ../../../../nvt_md.gro <<EOF
ri 225-242 & 8
name 18 225-242-sidechain
q
EOF

cd ..

mkdir 243-245
cd 243-245

gmx make_ndx -f ../../../../nvt_md.gro <<EOF
ri 243-245 & 8
name 18 243-245-sidechain
q
EOF

cd ..

mkdir 246-248
cd 246-248

gmx make_ndx -f ../../../../nvt_md.gro <<EOF
ri 246-248 & 8
name 18 246-248-sidechain
q
EOF

cd ..

mkdir 249-253
cd 249-253

gmx make_ndx -f ../../../../nvt_md.gro <<EOF
ri 249-253 & 8
name 18 249-253-sidechain
q
EOF

cd ..

mkdir 254-262
cd 254-262

gmx make_ndx -f ../../../../nvt_md.gro <<EOF
ri 254-262 & 8
name 18 254-262-sidechain
q
EOF

cd ..

mkdir 264-267
cd 264-267

gmx make_ndx -f ../../../../nvt_md.gro <<EOF
ri 264-267 & 8
name 18 264-267-sidechain
q
EOF

cd ..

mkdir 268-287
cd 268-287

gmx make_ndx -f ../../../../nvt_md.gro <<EOF
ri 268-287 & 8
name 18 268-287-sidechain
q
EOF

cd ..

mkdir 309-317
cd 309-317

gmx make_ndx -f ../../../../nvt_md.gro <<EOF
ri 309-317 & 8
name 18 309-317-sidechain
q
EOF

cd ..