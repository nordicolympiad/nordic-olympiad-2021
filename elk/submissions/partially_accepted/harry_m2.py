#!/usr/bin/python3

n,m,a,b = map(int,input().split())

edges = [[] for _ in range(n)]

inp = []

for _ in range(m):
    x,y = map(int,input().split())
    edges[x].append(y)
    edges[y].append(x)
    inp.append((x,y))

# Hitta den koraste pathen mellan a och b
parent = [-1]*n
parent[a] = a
BFS = [a]
for curr in BFS:
    for nei in edges[curr]:
        if parent[nei] == -1:
            parent[nei] = curr
            BFS.append(nei)
        if nei == b:
            BFS = []
            break

# Markera noderna på pathen
onpath = [0]*n
curr = b
while curr != a:
    onpath[curr] = 1
    curr = parent[curr]
    onpath[curr] = 1


def findBridges(edgeList,n): #O(m^2)
    edges = [[] for _ in range(n)]
    for x,y in edgeList:
        edges[x].append(y)
        edges[y].append(x)
    visited = [0]*n

    components = 0
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = 1
        components += 1
        
        BFS = [i]
        for curr in BFS:
            for nei in edges[curr]:
                if visited[nei]:
                    continue
                visited[nei] = 1
                BFS.append(nei)
    #print(components)
    out = []
    for id in range(len(edgeList)):
        edges = [[] for _ in range(n)]
        for ind,(x,y) in enumerate(edgeList):
            if id == ind:
                continue
            edges[x].append(y)
            edges[y].append(x)
        
        visited = [0]*n

        #print(edges)
        comps = 0
        for i in range(n):
            if visited[i]:
                continue
            visited[i] = 1
            comps += 1
            
            BFS = [i]
            for curr in BFS:
                for nei in edges[curr]:
                    if visited[nei]:
                        continue
                    visited[nei] = 1
                    BFS.append(nei)
        
        if comps > components:
            #print(comps)
            out.append(id)
    return out


banned = findBridges(inp,n)
okay = [1]*m
for x in banned:
    okay[x] = 0

newEdges = [[] for _ in range(n)]
for i,(x,y) in enumerate(inp):
    if okay[i]:
        newEdges[x].append(y)
        newEdges[y].append(x)

visited = [0]*n
for i in range(n):
    if onpath[i] == 0:
        continue
    if visited[i]:
        continue
    visited[i] = 1
    BFS = [i]

    for curr in BFS:
        for nei in newEdges[curr]:
            if visited[nei]:
                continue
            visited[nei] = 1
            onpath[nei] = 1
            BFS.append(nei)


out = []

for i in range(n):
    if onpath[i]:
        continue
    out.append(i)

print(len(out))
#print(*out)
for x in out:
    print(x)

