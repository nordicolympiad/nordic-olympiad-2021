#!/bin/bash

PPATH=$(realpath ..)

. ../../testdata_tools/gen.sh

use_solution harry.py

compile gen_random.py
compile gen_tree.py


samplegroup
sample 1
sample 2


#  $1$    & $10$       & $N \le 10$, $M \le 45$  \\ \hline
#  $2$    & $20$       & $M = N-1$ and the graph is connected. \\ \hline
#  $3$    & $30$       & $N \le 200$, $M \le 500$ \\ \hline
#  $4$    & $40$       & No additional constraints. \\ \hline

#Relevanta träd modes: "line" "killCubic" "deep" "deeper" "random"

group group1 10
limits maxN=10 maxM=45
include_group sample
tc g1-edge1 gen_tree n=2
tc g1-edge2 gen_tree n=3
tc g1-edge3 gen_tree n=4
tc g1-line gen_tree n=10 modeTree='line'
tc g1-tree1 gen_tree n=10 modeTree='random'
tc g1-tree2 gen_tree n=10 modeTree='deep'
tc g1-random01 gen_random n=3 m=3
tc g1-random02 gen_random n=4 m=6 
tc g1-random03 gen_random n=5 m=5 dist=2
tc g1-random04 gen_random n=10 m=45 
tc g1-random05 gen_random n=10 m=20 dist=9
tc g1-random06 gen_random n=10 dist=5
tc g1-random07 gen_random n=10 m=5 dist=3

group group2 20
limits mode="tree"
tc g1-edge1
tc g1-edge2
tc g1-edge3
tc g1-line
tc g1-tree1
tc g1-tree2
tc g2-small1 gen_tree n=200 modeTree='line'
tc g2-small2 gen_tree n=200 modeTree='line' a=145 b=144
tc g2-small3 gen_tree n=200 modeTree='random' 
tc g2-small4 gen_tree n=200 modeTree='deep' a=0 b=199
tc g2-small5 gen_tree n=200 modeTree='deeper'
tc g2-small6 gen_tree n=200 modeTree='killCubic'
tc g2-line1 gen_tree n=50000 modeTree='line'
tc g2-line2 gen_tree n=50000 modeTree='line' a=12345 b=12346
tc g2-line3 gen_random n=50000 m=49999 dist=49999
tc g2-random1 gen_tree n=50000 modeTree='random'
tc g2-random2 gen_tree n=50000 modeTree='random'
tc g2-deep1 gen_tree n=50000 modeTree='deep'
tc g2-deeper gen_tree n=50000 modeTree='deeper'
tc g2-cubic gen_tree n=50000 modeTree='killCubic'
tc g2-cubic2 gen_tree n=50000 modeTree='killCubic'
tc g2-deep2 gen_tree n=50000 modeTree='deep' a=0 b=49999
tc g2-line4 gen_tree n=50000 modeTree='line' a=1 b=49998


group group3 30
limits maxN=200 maxM=500
include_group group1
tc g2-small1
tc g2-small2
tc g2-small3
tc g2-small4
tc g2-small5
tc g2-small6
tc g3-edge gen_random n=200 m=2
tc g3-random01 gen_random n=200 m=200 dist=100
tc g3-random02 gen_random n=200 m=100 dist=100
tc g3-random03 gen_random n=200 m=100 dist=50
tc g3-random04 gen_random n=200 m=500 dist=50
tc g3-random05 gen_random n=200 m=500 dist=199
tc g3-random06 gen_random n=200 m=500 

group group4 40
limits maxQ=10
include_group sample
include_group group2
include_group group3
tc g4-random01 gen_random n=50000 m=2 
tc g4-random02 gen_random n=50000 m=100 dist=5 
tc g4-random03 gen_random n=50000 m=10000 dist=7890
tc g4-random04 gen_random n=50000 m=100000 dist=1
tc g4-random05 gen_random n=50000 m=100000 dist=10000
tc g4-random06 gen_random n=50000 m=100000 dist=49999
tc g4-random07 gen_random n=50000 m=12345 dist=12345 
