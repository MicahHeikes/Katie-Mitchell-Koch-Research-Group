#!/bin/bash

cd resi
grep 'H-Bond' HB-Lifetime.txt > H-Bonds.txt
for file in H-Bonds.txt; do (cat "${file}"; echo) >> ../HB_Lifetimes.txt; done
rm H-Bonds.txt
cd ../
