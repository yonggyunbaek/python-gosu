# https://www.acmicpc.net/problem/12852

import sys
input = sys.stdin.readline

n = int(input())

dp = [0]*(n+1)

for i in range(2,n+1):
    
    # 1을 뺀 경우
    dp[i] = dp[i-1] + 1
    
    # 2로 나누어 떨어지면
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2]+1)
    
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3]+1)
    print(dp)
print(dp[n])

res = [n]
now = n
temp = dp[n] - 1

# n부터 하나씩 줄여나가면서 순서 찾기
for i in range(n, 0, -1):
    if dp[i] == temp and (i+1 == now or i*2 == now or i*3 == now):
        now = i
        res.append(i)
        temp -= 1
    print(res, now, temp)

print(*res)