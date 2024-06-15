#!/usr/bin/python3

na,nb,k,q = map(int,input().split())
a = input()
b = input()
edges = [set() for _ in range(ord("z")-ord("a")+1)]
for _ in range(k):
    x,y = input().split()
    edges[ord(x)-ord("a")].add(y)


necklace = []

for i in range(na):
    for j in range(nb):
        if b[j] in edges[ord(a[i])-ord("a")]:
            continue
        necklace.append(a[i])
        necklace.append(b[j])


for _ in range(q):
    print(necklace[int(input())])
