# https://www.acmicpc.net/problem/9934

import sys
input = sys.stdin.readline

K = int(input())
building = list(map(int,input().split()))
result = [[] for _ in range(K)]

def find(start, end, level):
    if start > end:
        return None
    mid = (start + end) // 2
    result[level].append(building[mid])
    find(start, mid-1, level+1)
    find(mid+1, end, level+1)

find(0, len(building)-1, level=0)

for i in result:
    print(*i)