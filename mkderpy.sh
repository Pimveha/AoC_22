#!/bin/bash

daydir="day_$1"
mkdir $daydir

cp template.py $daydir/p.py

# subl $daydir/input

# cd ./$daydir
open ./$daydir
subl $daydir/input