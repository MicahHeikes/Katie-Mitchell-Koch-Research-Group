#!/bin/bash

# Every "for" loop will need to be modified to fit your simulation.  Change n in {1..n} to the number
# of msd.xvg files you have.  For a 50ns trajectory, analyzed every 200ps, n=250 ((50000ps/200ps)=250)

# line 36 will also need a specific value, change (t2-t1) to fit what values you extract.  The script is set to 
# get values at 10ps and 40 ps, if using these values put (30) in place of (t2-t1)

for i in {1..n}
  do     
    grep "    10 \|    40 " msd${i}.xvg > msd$i.txt
  done

for i in {1..n}
  do     

ex msd${i}.txt <<EOEX
:%s/^.\{12}//
:wq 
EOEX

  done

for i in {1..n}
  do     
    awk 'NR==1{v=$1}{$1-=v}1' msd${i}.txt > sub$i.txt
  done

for i in {1..n}
  do     
    awk '($1!=0)' sub${i}.txt > dist$i.txt
  done

for i in {1..n}
  do     
    awk '{print $1/(t2-t1)}' dist${i}.txt > slope$i.txt
  done

for i in {1..n}
  do     
    awk '{print $1/(100)}' slope${i}.txt > cm2pers$i.txt
  done

for i in {1..n}
  do     
    awk '{print $1/(6)}' cm2pers${i}.txt > Diffusion_Coef$i.doc
  done

rm *.txt

for file in *.doc; do (cat "${file}"; echo) >> Diffusion_Coe.txt; done

grep . Diffusion_Coe.txt > Diffusion_Coefficients.txt

rm Diffusion_Coe.txt

awk '{ total += $1 } END { print total/NR }' Diffusion_Coefficients.txt > Average_Diffusion_Coefficient.txt

rm *.doc

for file in Average_Diffusion_Coefficient.txt; do (cat "${file}"; echo) >> ../Diffusion_Co.txt; done