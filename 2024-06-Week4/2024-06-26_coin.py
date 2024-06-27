# https://www.acmicpc.net/problem/11047

import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coin = []
for _ in range(N):
    num = int(input())
    if num <= K:
        coin.append(num)

ans = 0
for value in reversed(coin):
    ans += K // value
    K %= value
    if K == 0:
        break

print(ans)


