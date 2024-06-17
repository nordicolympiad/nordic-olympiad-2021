#!/usr/bin/python3

import math
import sys
import random

checked = set()

def cmdlinearg(name, default=None):
    checked.add(name)
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    if default is None:
        print("missing parameter", name)
        sys.exit(1)
    return default

def gen_tree(mode,n):
    eds = []
    depth = [0]
    adj = [[] for _ in range(n)]
    if mode== 'line':
        for i in range(0,n-1):
            eds.append((i,i+1))
    elif mode== 'killCubic':
        for i in range(2*(n//3)):
            eds.append((i,i+1))
        eds.append((2*(n//3)+1,n//3))
        for i in range(2*(n//3)+1,n-1):
            eds.append((i,i+1))
    else:
        for i in range(1, n):
            while True:
                if mode == 'random':
                    pred = random.randrange(i)
                elif mode == 'deep':
                    pred = i-1 - int(random.uniform(0, i**0.1) ** 10)
                elif mode == 'deeper':
                    if i < 4:
                        pred = random.randrange(i)
                    else:
                        hi = math.log2(math.log2(i))
                        pred = i - int(2 ** 2 ** min(random.uniform(-3, hi), random.uniform(-3, hi), random.uniform(-3, hi)))
                else:
                    assert False, f"unknown mode {mode}"
                assert 0 <= pred < i
                if len(adj[pred]) < 3:
                    break
            adj[pred].append(i)
            adj[i].append(pred)
            eds.append((pred, i))
            depth.append(depth[pred] + 1)
    return eds, adj


#Relevanta: "line" "killCubic" "deep" "deeper" "random"
modeTree=cmdlinearg('modeTree','random')
n=int(cmdlinearg('n'))
a=int(cmdlinearg('a',random.randint(0,n-1)))
b=int(cmdlinearg('b',random.randint(0,n-1)))

while a == b: # Make sure a != b
    a,b = random.randint(0,n-1),random.randint(0,n-1)

endAtOne=int(cmdlinearg('endAtOne',0))
random.seed(int(cmdlinearg('seed', sys.argv[-1])))

print(n,n-1,a,b)

eds, _ = gen_tree(modeTree,n)


edges = [[] for _ in range(n)]
for i,j in eds:
    print(i,j)



for arg in sys.argv[1:-1]:
    assert '=' in arg
    assert arg.split('=')[0] in checked, arg