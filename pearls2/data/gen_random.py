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

la = int(arg('la', 2*10**5))
lb = int(arg('lb', 2*10**5))
k = int(arg('k', random.randint(0,26**2-1)))
q = int(arg('q', 10**5))

alpha = int(arg('alpha',26))
shift = random.randint(0,26-alpha)
alphabet = [chr(x+ord("a") + shift) for x in range(alpha)]

print(la,lb,k,q)

a = [random.choice(alphabet) for _ in range(la)]
b = [random.choice(alphabet) for _ in range(lb)]
print("".join(a))
print("".join(b))

pairs = []
used = set()
while len(pairs) < k:
    x,y = random.randint(0,25),random.randint(0,25)
    if (x,y) in used:
        continue
    pairs.append([chr(x+ord("a")),chr(y+ord("a"))])
    used.add((x,y))

for x,y in pairs:
    print(x,y)



def calcMaxInd(a,b,pairs):
    edges = [set() for _ in range(ord("z")-ord("a")+1)]
    for x,y in pairs:
        edges[ord(x)-ord("a")].add(y)

    chars = []
    prefixes = []
    for ch in range(ord("z")-ord("a")+1):
        temp = []

        for x in b:
            if x in edges[ch]:
                temp.append(0)
            else:
                temp.append(1)
        
        chars.append(temp)

        p = [0]
        for v in temp:
            p.append(v+p[-1])
        prefixes.append(p)


    necklacesCnt = [prefixes[ord(x)-ord("a")][-1] for x in a]
    necklacePrefix = [0]
    for v in necklacesCnt:
        necklacePrefix.append(necklacePrefix[-1]+v)
    
    return necklacePrefix[-1]

maxInd = calcMaxInd(a,b,pairs)*2 - 1 

assert(maxInd > 0)

queries = []
if mode != "even":
    queries.append(maxInd)

while len(queries) < q:
    t = random.randint(0,maxInd)
    if mode == "even":
        t -= t%2
    elif mode == "odd":
        t += (t%2 == 0)

    queries.append(t)


random.shuffle(queries)
for x in queries:
    print(x)


