# https://www.acmicpc.net/problem/2890

import sys
input = sys.stdin.readline

r, c = map(int, input().rstrip().split())
kayak = [list(input().rstrip()) for _ in range(r)]
result = []
for i in range(r):
    for k in range(1, 10):
        if kayak[i].count(str(k)) > 0:
            cnt = 0
            for j in range(c-1, -1, -1):
                if kayak[i][j] == str(k):
                    break
                cnt += 1
            result.append([cnt, k, 0])

result.sort(key=lambda x:x[0])
result[0][2] = 1
now = 1
for i in range(1, len(result)):
    if result[i][0] != result[i-1][0]:
        now += 1
    result[i][2] = now
result.sort(key=lambda x:x[1])
for i in range(len(result)):
    print(result[i][2])
