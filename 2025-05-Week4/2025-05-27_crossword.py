# https://www.acmicpc.net/problem/3005

from collections import defaultdict
import heapq
import sys
input = sys.stdin.readline

r, c = map(int,input().split())

cword = defaultdict(str)
wlist = []
for i in range(r):
    word = input().rstrip()
    if '#' not in word:
        heapq.heappush(wlist, word)
    else:
        for i in word.split('#'):
            if len(i) >= 2:
                heapq.heappush(wlist, i)
    for j in range(c):
        cword[j] += (word[j])

for k,v in cword.items():
    if '#' not in v:
        heapq.heappush(wlist, v)
    else:
        for i in v.split('#'):
            if len(i) >= 2:
                heapq.heappush(wlist, i)


print(heapq.heappop(wlist))
