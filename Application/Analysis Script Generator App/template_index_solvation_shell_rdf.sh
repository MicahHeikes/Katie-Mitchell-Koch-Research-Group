#!/bin/bash

mkdir resi
cd resi

gmx make_ndx -f ../../../grofile <<EOF
ri resi & 8
name 18 resi-sidechain
q
EOF
cd ..
