# https://www.acmicpc.net/problem/2108

import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
numlst = [ int(input()) for _ in range(n) ]
numdict = Counter(numlst)
maxv = max(numdict.values())
result = filter(lambda x:x[1] == maxv, numdict.items())
kv = sorted([i for i in result], key=lambda x:x[0])

roundv = 0

mean = f"{(sum(numlst) / n):.0f}"
print(int(mean))
print(sorted(numlst)[n//2])
if len(kv) != 1:
    print(kv[1][0])
else:
    print(kv[0][0])
print(max(numlst)-min(numlst))

