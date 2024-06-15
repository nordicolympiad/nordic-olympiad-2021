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
tc g1-small01 gen_random la=1 lb=10 k=0 q=10
tc g1-small02 gen_random la=1 lb=10 k=250 q=10
tc g1-small03 gen_random la=1 lb=1 k=1 q=10
tc_manual ../manual/manual-small.in
tc g1-medium01 gen_random la=1 lb=995 k=300 q=100000 mode="even"
tc g1-medium02 gen_random la=1 lb=1000 k=400 q=100000 
tc g1-medium03 gen_random la=1 lb=1000 k=200 q=100000 mode="odd"
tc g1-large01 gen_random la=1 lb=100000 k=400 q=10 mode="even"
tc g1-large02 gen_random la=1 lb=99966 k=300 q=100000 
tc g1-large03 gen_random la=1 lb=100000 k=300 q=100000 mode="odd"

group group2 9
limits maxA=1000 maxB=1000
tc g1-small01
tc g1-small02
tc g1-small03
tc manual-small
tc g1-medium01
tc g1-medium02
tc g1-medium03
tc g2-small01 gen_random la=10 lb=10 k=0 q=10
tc g2-small02 gen_random la=10 lb=10 q=10
tc g2-large01 gen_random la=997 lb=998 q=10 k=600 mode="odd"
tc g2-large02 gen_random la=1000 lb=1000 q=100000 k=0 mode="odd"
tc g2-large03 gen_random la=1000 lb=996 q=100000 mode="odd"
tc g2-large04 gen_random la=998 lb=1000 q=100000 k=600 
tc g2-large05 gen_random la=1000 lb=1000 q=100000 k=600 mode="odd"

group group3 13
limits maxK=0
tc g1-small01
tc g2-small01
tc g2-large02
tc g3-01 gen_random q=10 k=0 
tc g3-02 gen_random q=100000 k=0 
tc g3-03 gen_random la=100000 lb=100000 q=100000 k=0 
tc g3-04 gen_random la=100000 lb=100000 q=100000 k=0 mode="odd"

group group4 15
limits maxQ=10
tc g1-small01
tc g1-small02
tc g1-small03
tc manual-small
tc g1-large01
tc g2-small01
tc g2-small02
tc g2-large01
tc g3-01
tc g4-01 gen_random q=10  
tc g4-02 gen_random q=10 k=675 
tc g4-03 gen_random la=100000 lb=100000 q=10  
tc g4-04 gen_random la=100000 lb=100000 q=10 mode="odd" 

group group5 56
include_group group1
include_group group2
include_group group3
include_group group4
tc g5-01 gen_random
tc g5-02 gen_random mode="odd"
tc g5-03 gen_random k=675 
tc g5-04 gen_random la=100000 lb=100000 q=100000
tc g5-05 gen_random la=100000 lb=100000 q=100000 mode="odd" 