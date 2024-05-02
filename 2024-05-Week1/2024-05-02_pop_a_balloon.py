# https://www.acmicpc.net/problem/2346

from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
q = deque([(move, idx + 1) for idx, move in enumerate(arr)])

idx = 0
ans = []
while q:
    print(q)
    (v, i) = q.popleft()
    print(v, i)
    ans.append(i)
    if v > 0:
        # rotate(양수) 오른쪽으로
        # rotate(음수) 왼쪽으로
        q.rotate(1-v)
    else:
        q.rotate(-v)
for a in ans:
    print(a, end=' ')
    


