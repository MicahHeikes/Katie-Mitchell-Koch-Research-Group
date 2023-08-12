#!/bin/bash

cd resi
grep 'Average' Block_Averaging_20Blocks.txt > Averages.txt
for file in Averages.txt; do (cat "${file}"; echo) >> ../Diffusion_Averages.txt; done
rm Averages.txt
cd ../
