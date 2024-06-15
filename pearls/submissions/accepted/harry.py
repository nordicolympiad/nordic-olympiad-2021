#!/usr/bin/python3

na,nb,k,q = map(int,input().split())
a = input()
b = input()
edges = [set() for _ in range(ord("z")-ord("a")+1)]
for _ in range(k):
    x,y = input().split()
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



# för varje query, binärsöka index i A, och sedan binärsöka index i B
for _ in range(q):
    curr = int(input())
    
    pairInd = curr//2+1


    l = 1
    r = len(a)
    while l<r:
        m = (l+r)//2
        if necklacePrefix[m] >= pairInd:
            r = m
        else:
            l = m+1
    
    charind = l-1
    if curr % 2 == 0:
        print(a[charind])
    else:
        pref = prefixes[ord(a[charind])-ord("a")]

        l = 1
        r = len(a)
        pairInd -= necklacePrefix[charind]
        
        while l<r:
            m = (l+r)//2
            if pref[m] >= pairInd:
                r = m
            else:
                l = m+1

        print(b[l-1])
