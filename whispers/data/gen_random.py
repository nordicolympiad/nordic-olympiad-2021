#!/usr/bin/python3

import math
import sys
import random

def arg(name, default=None):
    for arg in sys.argv:
        if arg.startswith(name + "="):
            return arg.split("=")[1]
    assert default is not None, name
    return default



random.seed(int(arg('seed', sys.argv[-1])))

mode = arg('mode','random')

n = int(arg('n', random.randint(2,20)))
m = int(arg('m', random.randint(2,1000)))

a = random.randint(0,n-1)
b = random.randint(n*m-n,n*m-1)

graph = [[] for _ in range(n*m)]

usedEdges = set()

# Generate base edges
for i in range(m-1):
    poss = [*range((i+1)*n,(i+2)*n)]
    random.shuffle(poss)

    for j in range(n):
        graph[j+i*n].append(poss.pop())
        usedEdges.add((j+i*n,graph[j+i*n][-1]))

# (m-1)*n

maxEdges = (m-1)*n*n

K = int(arg('K',min(5000,maxEdges)))


if mode == "random":
    while len(usedEdges) < K:
        start = random.randint(0,m-2)*n 
        nxt = start+n
        
        start += random.randint(0,n-1)
        nxt += random.randint(0,n-1)
        if (start,nxt) in usedEdges:
            continue
        else:
            usedEdges.add((start,nxt))
            graph[start].append(nxt)
elif mode == "empty":
    pass

print(n,m,a,b)
for i in range(n*(m-1)):
    random.shuffle(graph[i])
    print(len(graph[i]),*graph[i])    
    



