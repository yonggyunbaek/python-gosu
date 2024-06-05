# https://www.acmicpc.net/problem/9625

import sys
input = sys.stdin.readline

K = int(input())
ans = []
for i in range(K+1):
    if i == 0:
        ans.append([1,0])
    elif i == 1:
        ans.append([0,1])
    else:
        ans.append([ans[i-1][0]+ans[i-2][0], ans[i-1][1]+ans[i-2][1]])

print(*ans[K])


