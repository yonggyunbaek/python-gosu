# https://www.acmicpc.net/problem/1966

import sys
from collections import deque
input = sys.stdin.readline

case = int(input())

for _ in range(case):
    cnt = 0
    N, M = map(int, input().split())
    importance = deque(map(int, input().split()))
    v = importance[M]
    while importance:
        # print(importance, M, v, cnt)
        if importance[0] == max(importance):
            k = importance.popleft()
            cnt += 1
            if k == v and M == 0:
                break
            
            M -= 1
            if M < 0:
                M = len(importance)-1
            
        else:
            importance.append(importance.popleft())
            M -= 1
            if M < 0:
                M = len(importance)-1
    print(cnt)