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

#Relevanta: "line" "killCubic" "deep" "deeper" "random"

group group1 10
limits maxN=10 maxM=45
include_group sample
tc g1-edge1 gen_tree n=2
tc g1-edge2 gen_tree n=3
tc g1-edge3 gen_tree n=4
tc g1-line gen_tree n=10 modeTree='line'
tc g1-tree1 gen_tree n=10 modeTree='random'
tc g1-tree2 gen_tree n=10 modeTree='deep'
# TODO a case where M < N


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
tc g2-small4 gen_tree n=200 modeTree='deep'
tc g2-small5 gen_tree n=200 modeTree='deeper'
tc g2-small6 gen_tree n=200 modeTree='killCubic'
tc g2-line1 gen_tree n=50000 modeTree='line'
tc g2-line2 gen_tree n=50000 modeTree='line' a=12345 b=12346
tc g2-random1 gen_tree n=50000 modeTree='random'
tc g2-random2 gen_tree n=50000 modeTree='random'
tc g2-deep gen_tree n=50000 modeTree='deep'
tc g2-deeper gen_tree n=50000 modeTree='deeper'
tc g2-cubic gen_tree n=50000 modeTree='killCubic'
tc g2-cubic2 gen_tree n=50000 modeTree='killCubic'

group group3 30
limits maxN=200 maxM=500
include_group group1
tc g2-small1
tc g2-small2
tc g2-small3
tc g2-small4
tc g2-small5
tc g2-small6


group group4 40
limits maxQ=10
include_group sample
include_group group2
include_group group3
