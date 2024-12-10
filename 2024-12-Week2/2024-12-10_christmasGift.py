# https://www.acmicpc.net/problem/14235/


import heapq
import sys

input = sys.stdin.readline

n = int(input())
gift = []
for i in range(n):
    nums = list(map(int, input().split()))
    a = nums[0]    
    if a == 0 and len(gift) == 0:
        print(-1)
    elif a == 0 and len(gift) != 0:
        print(heapq.heappop(gift)*-1)
    else:
        for num in nums[1:]:
            heapq.heappush(gift, -num) 
