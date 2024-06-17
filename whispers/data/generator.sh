#!/bin/bash

PPATH=$(realpath ..)

. ../../testdata_tools/gen.sh

use_solution harry.py

compile gen_random.py


samplegroup
sample 1
sample 2


#  $1$    & $18$       & $N = 2$  \\ \hline
#  $2$    & $16$       & $M = 3$, $N \le 8$\\ \hline
#  $3$    & $19$       & $M = 3$ \\ \hline
#  $4$    & $47$       & No additional constraints. \\ \hline


group group1 18
limits maxN=2
tc 1
tc g1-small01 gen_random n=2 m=2 K=2
tc g1-small02 gen_random n=2 m=2 K=3
tc g1-small03 gen_random n=2 m=2 K=4
tc g1-small04 gen_random n=2 m=3 K=4
tc g1-small05 gen_random n=2 m=3 K=6
tc g1-small06 gen_random n=2 m=3 K=8
tc g1-medium01 gen_random n=2 m=10 K=18
tc g1-medium02 gen_random n=2 m=50 K=98
tc g1-medium03 gen_random n=2 m=100 K=200
tc g1-medium04 gen_random n=2 m=500 K=1450
tc g1-medium05 gen_random n=2 m=501 
tc g1-large01 gen_random n=2 m=999  
tc g1-large02 gen_random n=2 m=1000 K=1998
tc g1-large03 gen_random n=2 m=1000 K=3000 
tc g1-large04 gen_random n=2 m=1000 K=2345


group group2 16
limits maxM=3 minM=3 maxN=8
include_group sample
tc g1-small04 
tc g1-small05
tc g1-small06 


group group3 19
limits maxM=3 minM=3
include_group group2


group group4 47
include_group sample
include_group group1
include_group group2
include_group group3

