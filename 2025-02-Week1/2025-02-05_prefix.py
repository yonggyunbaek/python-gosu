# https://www.acmicpc.net/problem/14426

import sys
input = sys.stdin.readline

n,m = map(int,input().split())
s = [ input().rstrip() for _ in range(n) ]
cnt = 0

# for _ in range(m):
#     p = input().rstrip()
#     l = len(p)
#     for i in s:
#         if i[:l] == p:
#             cnt += 1
#             break
# print(cnt)

for _ in range(m):
    p = input().rstrip()
    for i in s:
        if i.startswith(p):
            cnt += 1
            break
print(cnt)