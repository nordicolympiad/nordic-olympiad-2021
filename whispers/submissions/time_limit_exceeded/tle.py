#!/usr/bin/python3

# O(2^n*m) because the sus-array had multiple identical elements

# https://github.com/cheran-senthil/PyRival/blob/master/pyrival/graphs/hopcroft_karp.py
def hopcroft_karp(graph, n, m):
    """
    Maximum bipartite matching using Hopcroft-Karp algorithm, running in O(|E| sqrt(|V|))
    """
    assert (n == len(graph))
    match1 = [-1] * n
    match2 = [-1] * m

    # Find a greedy match for possible speed up
    for node in range(n):
        for nei in graph[node]:
            if match2[nei] == -1:
                match1[node] = nei
                match2[nei] = node
                break
    while 1:
        bfs = [node for node in range(n) if match1[node] == -1]
        depth = [-1] * n
        for node in bfs:
            depth[node] = 0

        for node in bfs:
            for nei in graph[node]:
                next_node = match2[nei]
                if next_node == -1:
                    break
                if depth[next_node] == -1:
                    depth[next_node] = depth[node] + 1
                    bfs.append(next_node)
            else:
                continue
            break
        else:
            break

        pointer = [len(c) for c in graph]
        dfs = [node for node in range(n) if depth[node] == 0]
        while dfs:
            node = dfs[-1]
            while pointer[node]:
                pointer[node] -= 1
                nei = graph[node][pointer[node]]
                next_node = match2[nei]
                if next_node == -1:
                    # Augmenting path found
                    while nei != -1:
                        node = dfs.pop()
                        match2[nei], match1[node], nei = node, nei, match1[node]
                    break
                elif depth[node] + 1 == depth[next_node]:
                    dfs.append(next_node)
                    break
            else:
                dfs.pop()
    return match1, match2


n,m,a,b = map(int,input().split())

parent = [[] for _ in range(n*m)]

sus = [a]
for i in range(m-1):
    
    nxtSus = []


    graph = [[*map(lambda x: int(x)%n, input().split())][1:] for _ in range(n)]

    for curr in sus:
        for choice in graph[curr]:
            graphCopy = [[] for _ in range(n)]
            for u in range(n):
                if u == curr:
                    continue
                for v in graph[u]:
                    if v == choice:
                        continue
                    graphCopy[u].append(v)

            res1,res2 = hopcroft_karp(graphCopy,n,n)
            
            if res1.count(-1) == 1:
                parent[i*n+n+choice].append(i*n + curr)


                nxtSus.append(choice)

    
    sus,nxtSus = nxtSus,sus

#print(parent)

BFS = [b]
couldBeSus = [0]*(n*m)
couldBeSus[b] = 1

for curr in BFS:
    for nei in parent[curr]:
        if couldBeSus[nei]:
            continue
        couldBeSus[nei] = 1
        BFS.append(nei)


BFS.sort()

print(len(BFS))
for x in BFS:
    print(x)
    

