#!/usr/bin/python3

# Should only get 20p

n,m,a,b = map(int,input().split())

edges = [[] for _ in range(n)]

for _ in range(m):
    x,y = map(int,input().split())
    edges[x].append(y)
    edges[y].append(x)


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

onpath = [0]*n
curr = b
while curr != a:
    onpath[curr] = 1
    curr = parent[curr]
    onpath[curr] = 1

out = []

for i in range(n):
    if onpath[i]:
        continue
    out.append(i)

print(len(out))
#print(*out)
for x in out:
    print(x)

