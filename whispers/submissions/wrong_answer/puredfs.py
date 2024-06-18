#!/usr/bin/python3
import random


# Idea for WA:
# DFS from A. If reach B, add all of the nodes on the to output.

n,m,a,b = map(int,input().split())

out = set([a,b])


graph = [[] for _ in range(n*m)]
for i in range(n*(m-1)):
    for j in [*map(int,input().split())][1:]:
        graph[i].append(j)

for _ in range(1000):
    path = [a]

    while path[-1] != b:
        if len(graph[path[-1]]) == 0:
            break
        path.append(graph[path[-1]][random.randint(0,len(graph[path[-1]])-1)])
    else:
        for x in path:
            out.add(x)


out = list(out)


out.sort()
print(len(out))
for x in out:
    print(x)
    