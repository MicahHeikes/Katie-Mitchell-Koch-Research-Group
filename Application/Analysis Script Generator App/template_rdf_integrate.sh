#!/bin/bash

cd resi
gmx analyze -f rdf.xvg -integrate -e 0.6
cd ../ 
