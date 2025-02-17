# https://www.acmicpc.net/problem/1431

import sys
input = sys.stdin.readline

n = int(input())
sn = []
# 길이 짧은거 먼저
# 숫자만 더해서 더 작은거 먼저
# 사전순 - 숫자가 알파벳보다 작다
for _ in range(n):
    s = input().rstrip()
    s_len = len(s)
    s_sum = sum([ int(i) for i in list(s) if i.isdigit()])
    sn.append((s_len, s_sum, s))

for i in sorted(sn):
    print(i[2])

