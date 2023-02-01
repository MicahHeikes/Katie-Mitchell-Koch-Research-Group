#!/bin/bash

# In details.txt, there are many columns we do not
# need.  These first 16 colums list the number of waters
# at each snapshot in time.  We are only interested in 
# the assigned number of each water molecule present.
# This bash script deletes the first 16 columns.

cd 1-12
ex details.txt <<EOEX
:%s/^.\{16}//
:wq 
EOEX
cd ..

cd 13-18
ex details.txt <<EOEX
:%s/^.\{16}//
:wq 
EOEX
cd ..

cd 20-32
ex details.txt <<EOEX
:%s/^.\{16}//
:wq 
EOEX
cd ..

cd 44-57
ex details.txt <<EOEX
:%s/^.\{16}//
:wq 
EOEX
cd ..

cd 58-66
ex details.txt <<EOEX
:%s/^.\{16}//
:wq 
EOEX
cd ..

cd 67-75
ex details.txt <<EOEX
:%s/^.\{16}//
:wq 
EOEX
cd ..

cd 76-93
ex details.txt <<EOEX
:%s/^.\{16}//
:wq 
EOEX
cd ..

cd 94-98
ex details.txt <<EOEX
:%s/^.\{16}//
:wq 
EOEX
cd ..

cd 118-124
ex details.txt <<EOEX
:%s/^.\{16}//
:wq 
EOEX
cd ..

cd 142-146
ex details.txt <<EOEX
:%s/^.\{16}//
:wq 
EOEX
cd ..

cd 147-151
ex details.txt <<EOEX
:%s/^.\{16}//
:wq 
EOEX
cd ..

cd 162-169
ex details.txt <<EOEX
:%s/^.\{16}//
:wq 
EOEX
cd ..

cd 170-178
ex details.txt <<EOEX
:%s/^.\{16}//
:wq 
EOEX
cd ..

cd 184-211
ex details.txt <<EOEX
:%s/^.\{16}//
:wq 
EOEX
cd ..

cd 217-225
ex details.txt <<EOEX
:%s/^.\{16}//
:wq 
EOEX
cd ..

cd 225-242
ex details.txt <<EOEX
:%s/^.\{16}//
:wq 
EOEX

cd ..

cd 243-245
ex details.txt <<EOEX
:%s/^.\{16}//
:wq 
EOEX
cd ..

cd 246-248
ex details.txt <<EOEX
:%s/^.\{16}//
:wq 
EOEX
cd ..

cd 249-253
ex details.txt <<EOEX
:%s/^.\{16}//
:wq 
EOEX
cd ..

cd 254-262
ex details.txt <<EOEX
:%s/^.\{16}//
:wq 
EOEX
cd ..

cd 264-267
ex details.txt <<EOEX
:%s/^.\{16}//
:wq 
EOEX
cd ..

cd 268-287
ex details.txt <<EOEX
:%s/^.\{16}//
:wq 
EOEX
cd ..

cd 309-317
ex details.txt <<EOEX
:%s/^.\{16}//
:wq 
EOEX
cd ..
