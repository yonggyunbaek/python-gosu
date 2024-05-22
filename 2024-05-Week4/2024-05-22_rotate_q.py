# https://www.acmicpc.net/problem/1021

import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

q = deque( i for i in range(1,N+1) )
nums = list(map(int, input().split()))

cnt  = 0
for i in nums:
    while True:
        # 원하는 숫자 나오면 popleft
        if i == q[0]:
            q.popleft()
            break
        # 원하는 숫자 나올때까지 왼쪽이든 오른쪽이든 rotate 하면서 cnt += 1
        else:
            if q.index(i) > len(q) // 2:
                q.appendleft(q.pop())
                cnt += 1
            else:
                q.append(q.popleft())
                cnt += 1

print(cnt)