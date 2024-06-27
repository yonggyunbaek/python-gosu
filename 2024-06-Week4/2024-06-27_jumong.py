# https://www.acmicpc.net/problem/1940

import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
material = list(map(int,input().split()))

material.sort()
left, right = 0, len(material) -1
cnt = 0

while left < right:
    sum_num = material[left] + material[right]
    if sum_num < M:
        left += 1
    elif sum_num > M:
        right -= 1
    else:
        cnt += 1
        left += 1
        right -= 1

print(cnt)
