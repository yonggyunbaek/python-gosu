# https://www.acmicpc.net/problem/9461

import sys
input = sys.stdin.readline

plist = [1,1,1,2,2]
for i in range(4,100):
    plist.append(plist[i] + plist[i-4])

t = int(input())
for _ in range(t):
    n = int(input())
    print(plist[n-1])
    
