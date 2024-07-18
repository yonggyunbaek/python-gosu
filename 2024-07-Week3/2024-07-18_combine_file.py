# https://www.acmicpc.net/problem/13975

import sys
import heapq
input = sys.stdin.readline

# T개의 테스트 데이터
T = int(input())

for _ in range(T):
    # 소설 챕터 수
    K = int(input())
    # 챕터 별 크기
    ksize = list(map(int,input().split()))
    heapq.heapify(ksize)
    sum = 0
    while len(ksize) != 1:
        a = heapq.heappop(ksize)
        b = heapq.heappop(ksize)
        sum += (a+b)
        heapq.heappush(ksize, a+b)
        # print(ksize)
    print(sum)
