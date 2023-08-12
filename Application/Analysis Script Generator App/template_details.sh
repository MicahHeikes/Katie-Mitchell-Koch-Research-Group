#!/bin/bash

cd resi
ex details.txt <<EOEX
:%s/^.\{16}//
:wq 
EOEX
cd ..
