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

mode = arg('mode','none')

n = int(arg('n', 5*10**4))
m = int(arg('m', random.randint(2,min(10**5,n*(n-1)//2))))

assert m <= n*(n-1)//2

dist = int(arg('dist',random.randint(1,min(n-1,m)))) # Distance between a and b

usedEdges = set()


graph = [[] for _ in range(n)]

a = random.randint(0,n-1) # Random starting node

unused = []
for i in range(n):
    if i != a: unused.append(i)
random.shuffle(unused)

curr = a
while len(usedEdges) < dist:
    nxt = unused.pop()
    if nxt < curr:
        usedEdges.add((nxt,curr))
    else:
        usedEdges.add((curr,nxt))

    curr = nxt

b = curr 


while len(usedEdges) < m:
    
    x,y = random.randint(0,n-1), random.randint(0,n-1)
    if x == y:
        continue
    if y < x:
        x,y=y,x
    
    usedEdges.add((x,y))


print(n,m,a,b)

out = list(usedEdges)
random.shuffle(out)
for x,y in out:
    if random.randint(0,1):
        print(x,y)
    else:
        print(y,x)
    
    



