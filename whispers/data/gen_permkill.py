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
m = int(arg('m', random.randint(3,1000)))

a = random.randint(0,n-1)

graph = [[] for _ in range(n*m)]

usedEdges = set()

currb = a

orgpath = [a]

# Generate base edges
for i in range(m-1):
    poss = [*range((i+1)*n,(i+2)*n)]
    random.shuffle(poss)

    for j in range(n):
        graph[j+i*n].append(poss.pop())
        usedEdges.add((j+i*n,graph[j+i*n][-1]))
    
    currb = graph[currb%n + i*n][0]
    orgpath.append(currb)

b = currb


# (m-1)*n
maxEdges = (m-1)*n*n

K = int(arg('K',min(5000,maxEdges)))


for i in range(m-2,-1,-1):
    if len(usedEdges) >= K:
        break

    currmain = orgpath[i]
    side1 = []
    side2 = []
    for j in range(i*n,(i+1)*n):
        if j == currmain:
            continue
        side1.append(j)
        side2.append(graph[j][0])
    
    for j in side2:
        if len(usedEdges) < K:
            assert((currmain,j) not in usedEdges)
            graph[currmain].append(j)
            usedEdges.add((currmain,j))
    
    while side1:
        side2.pop()
        curr = side1.pop()
        for j in side2:
            if len(usedEdges) < K:
                assert((curr,j) not in usedEdges)
                graph[curr].append(j)
                usedEdges.add((curr,j))
        


print(n,m,a,b)
for i in range(n*(m-1)):
    random.shuffle(graph[i])
    print(len(graph[i]),*graph[i])    
    



