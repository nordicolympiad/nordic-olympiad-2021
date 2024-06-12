#!/bin/bash

PPATH=$(realpath ..)

. ../../testdata_tools/gen.sh

use_solution harry.py

compile gen_random.py


samplegroup
sample 1
sample 2



# $1$    & $7$        & $L_A = 1$  \\ \hline
#  $2$    & $9$        & $L_A, L_B \le 1000$ \\ \hline
#  $3$    & $13$       & $k = 0$ \\ \hline
#  $4$    & $15$       & $q \le 10$ \\ \hline 
#  $5$    & $56$       & No additional constraints. \\ \hline


group group1 7
limits maxA=1

group group2 9
limits maxA=1000 maxB=1000

group group3 13
limits maxK=0

group group4 15
limits maxQ=10

group group5 56
include_group group1
include_group group2
include_group group3
include_group group4
