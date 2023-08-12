#!/bin/bash

cd resi
grep 'Optimized' optimized_parameters.txt > Optimizeds.txt
for file in Optimizeds.txt; do (cat "${file}"; echo) >> ../Optimized_Coefficients.txt; done
rm Optimizeds.txt
cd ../
