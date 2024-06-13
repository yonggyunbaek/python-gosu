# https://www.acmicpc.net/problem/9655

import sys
input = sys.stdin.readline

N = int(input())

# if N % 2 == 0:
#     print('CY')
# else:
#     print('SK')

# dp 
dp = [ 0 ] * (N+1)
for i in range(1,N+1):
    if i == 1:
        dp[1] = 1
    elif i ==2 :
        dp[2] = 2
    else:
        dp[i] = min( dp[i-1]+1 , dp[i-3] + 1)
    
if dp[N] % 2 != 0:
    print('SK')
else:
    print('CY')