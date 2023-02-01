#!/bin/bash

# This script will integrate each rdf.xvg plot out to 6 Angstroms, this will
# give us the population density in the first solvation shell.

cd 1-12
gmx analyze -f rdf.xvg -integrate -e 0.6
cd ../ 

cd 13-18
gmx analyze -f rdf.xvg -integrate -e 0.6
cd ../

cd 20-32
gmx analyze -f rdf.xvg -integrate -e 0.6
cd ../

cd 44-57
gmx analyze -f rdf.xvg -integrate -e 0.6
cd ../

cd 58-66
gmx analyze -f rdf.xvg -integrate -e 0.6
cd ../

cd 67-75
gmx analyze -f rdf.xvg -integrate -e 0.6
cd ../

cd 76-93
gmx analyze -f rdf.xvg -integrate -e 0.6
cd ../

cd 94-98
gmx analyze -f rdf.xvg -integrate -e 0.6
cd ../

cd 118-124
gmx analyze -f rdf.xvg -integrate -e 0.6
cd ../

cd 142-146
gmx analyze -f rdf.xvg -integrate -e 0.6
cd ../

cd 147-151
gmx analyze -f rdf.xvg -integrate -e 0.6
cd ../

cd 162-169
gmx analyze -f rdf.xvg -integrate -e 0.6
cd ../

cd 170-178
gmx analyze -f rdf.xvg -integrate -e 0.6
cd ../

cd 184-211
gmx analyze -f rdf.xvg -integrate -e 0.6
cd ../

cd 217-225
gmx analyze -f rdf.xvg -integrate -e 0.6
cd ../

cd 225-242
gmx analyze -f rdf.xvg -integrate -e 0.6
cd ../

cd 243-245
gmx analyze -f rdf.xvg -integrate -e 0.6
cd ../

cd 246-248
gmx analyze -f rdf.xvg -integrate -e 0.6
cd ../

cd 249-253
gmx analyze -f rdf.xvg -integrate -e 0.6
cd ../

cd 254-262
gmx analyze -f rdf.xvg -integrate -e 0.6
cd ../

cd 264-267
gmx analyze -f rdf.xvg -integrate -e 0.6
cd ../

cd 268-287
gmx analyze -f rdf.xvg -integrate -e 0.6
cd ../

cd 309-317
gmx analyze -f rdf.xvg -integrate -e 0.6
cd ../