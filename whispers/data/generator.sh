#!/bin/bash

PPATH=$(realpath ..)

. ../../testdata_tools/gen.sh

use_solution harry.py

compile gen_random.py
compile gen_permkill.py


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
tc g1-medium01 gen_random n=2 m=10 K=30
tc g1-medium02 gen_random n=2 m=50 K=98
tc g1-medium03 gen_random n=2 m=100 K=200
tc g1-medium04 gen_random n=2 m=500 K=1450
tc g1-medium05 gen_random n=2 m=501 
tc g1-large01 gen_random n=2 m=999  
tc g1-large02 gen_random n=2 m=1000 K=1998
tc g1-large03 gen_random n=2 m=1000 K=3000 
tc g1-large04 gen_random n=2 m=1000 K=2345
tc g1-antiperm01 gen_permkill n=2 m=1000 

# Min K = n*(m-1)
# Max K = n*n*(m-1)

group group2 16
limits maxM=3 minM=3 maxN=8
include_group sample
tc g1-small04 
tc g1-small05
tc g1-small06 
tc g2-random01 gen_random n=3 m=3 K=6
tc g2-random02 gen_random n=3 m=3 K=18
tc g2-random03 gen_random n=3 m=3 K=12
tc g2-random04 gen_random n=6 m=3 K=36
tc g2-random05 gen_random n=8 m=3 K=51
tc g2-random07 gen_random n=8 m=3 K=16
tc g2-random08 gen_random n=8 m=3 
tc g2-random09 gen_random n=8 m=3 K=100
tc g2-antiperm01 gen_permkill n=8 m=3 
tc g2-antiperm02 gen_permkill n=8 m=3 

group group3 19
limits maxM=3 minM=3
include_group group2
tc g3-small01 gen_random n=10 m=3 
tc g3-small02 gen_random n=10 m=3 K=60
tc g3-medium01 gen_random n=15 m=3 K=150
tc g3-medium02 gen_random n=17 m=3 K=40
tc g3-large01 gen_random n=20 m=3 K=40
tc g3-large02 gen_random n=20 m=3 K=100
tc g3-large03 gen_random n=20 m=3 K=600
tc g3-large04 gen_random n=20 m=3 K=798
tc g3-antiperm01 gen_permkill n=20 m=3
tc g3-antiperm02 gen_permkill n=20 m=3

group group4 47
include_group sample
include_group group1
include_group group2
include_group group3
tc g4-small01 gen_random n=4 m=4 K=13 
tc g4-small02 gen_random n=5 m=6 K=50 
tc g4-small03 gen_random n=5 m=123 K=1000 
tc g4-small04 gen_random n=8 m=342
tc g4-small05 gen_random n=4 m=1000 K=3996
tc g4-small06 gen_random n=5 m=1000 K=5000
tc g4-small07 gen_random n=4 m=1000 K=5000
tc g4-small08 gen_random n=3 m=1000 K=5000
tc g4-small09 gen_random n=3 m=1000 K=4002
tc g4-medium01 gen_random n=13 m=2 K=39
tc g4-medium02 gen_random n=15 m=15 K=1234
tc g4-medium03 gen_random n=16 m=14 
tc g4-medium04 gen_random n=12 m=400 
tc g4-large01 gen_random n=20 m=251  
tc g4-large02 gen_random n=20 m=200
tc g4-large03 gen_random n=20 m=11 K=3000
tc g4-large04 gen_random n=20 m=52 K=1984
tc g4-large05 gen_random n=19 m=260 
tc g4-large06 gen_random n=19 m=123
tc g4-large07 gen_random n=18 m=10 K=2901
tc g4-antiperm01 gen_permkill n=20 m=20
tc g4-antiperm02 gen_permkill n=20 m=40
tc g4-large08 gen_random n=20 m=13 
tc g4-large09 gen_random n=19 m=14