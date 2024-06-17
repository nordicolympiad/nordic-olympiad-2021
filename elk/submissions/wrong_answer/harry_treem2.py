#!/usr/bin/python3
#@EXPECTED_GRADES@ WA TLE WA WA


n,m,a,b = map(int,input().split())

edges = [[] for _ in range(n)]

for _ in range(m):
    x,y = map(int,input().split())
    edges[x].append(y)
    edges[y].append(x)


path = [[] for _ in range(n)]
path[a] = [a]
BFS = [a]

for curr in BFS:
    for nei in edges[curr]:
        if path[nei] == []:
            path[nei] = path[curr][:] + [nei]
            BFS.append(nei)
        if nei == b:
            BFS = []
            break

onpath = [0]*n
for x in path[b]:
    onpath[x] = 1

out = []

for i in range(n):
    if onpath[i]:
        continue
    out.append(i)

print(len(out))
#print(*out)
for x in out:
    print(x)

