#!/usr/bin/python3

# Baserat på Johans idé:
# 1. Lägg till en kant mellan a och b
# 2. Alla noder som inte är i samma biconnected component som a och b är i svaret.

"""
Given a directed graph, find_SCC returns a list of lists containing 
the strongly connected components in topological order.

Note that this implementation can be also be used to check if a directed graph is a
DAG, and in that case it can be used to find the topological ordering of the nodes.
"""
def find_SCC(graph):
    SCC, S, P = [], [], []
    depth = [0] * len(graph)
 
    stack = list(range(len(graph)))
    while stack:
        node = stack.pop()
        if node < 0:
            d = depth[~node] - 1
            if P[-1] > d:
                SCC.append(S[d:])
                del S[d:], P[-1]
                for node in SCC[-1]:
                    depth[node] = -1
        elif depth[node] > 0:
            while P[-1] > depth[node]:
                P.pop()
        elif depth[node] == 0:
            S.append(node)
            P.append(len(S))
            depth[node] = len(S)
            stack.append(~node)
            stack += graph[node]
    return SCC[::-1]

"""
Given an undirected simple graph, find_BCC returns a list of lists 
containing the edge biconnected components of the graph (i.e. no bridges).
Runs in O(n + m) time.

This algorithm is based on https://cses.fi/problemset/task/2177
"""
def find_BCC(graph):
    d = 0
    depth = [0] * len(graph)
    stack = list(range(len(graph)))
    while stack:
        node = stack.pop()
        if node < 0:
            d -= 1
        elif not depth[node]:
            d = depth[node] = d + 1
            stack.append(~node)
            stack += graph[node]
    
    graph2 = [[v for v in g if d + 2 > depth[v] != d - 1] for g,d in zip(graph, depth)]
    return find_SCC(graph2)



n,m,a,b = map(int,input().split())

edges = [[] for _ in range(n)]

for _ in range(m):
    x,y = map(int,input().split())
    edges[x].append(y)
    edges[y].append(x)

edges[a].append(b)
edges[b].append(a)


BCC = find_BCC(edges)
onpath = [0]*n

for comp in BCC:
    if a in comp or b in comp:
        for x in comp:
            onpath[x] = 1

out = []

for i in range(n):
    if not onpath[i]: out.append(i)


print(len(out))
for x in out:
    print(x)

