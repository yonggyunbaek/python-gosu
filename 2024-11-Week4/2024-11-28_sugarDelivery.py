# https://www.acmicpc.net/problem/2839

import sys
input = sys.stdin.readline

n = int(input())

dp = [-1] * (n+1)
dp[3] = 1
if n < 5:  
    print(dp[n])
else:
    dp[5] = 1
    for i in range(6,n+1):
        if i % 5 == 0:
            dp[i] = i // 5
            # print(i,"5배수",dp)
        else:
            if dp[i-5] == -1 and dp[i-3] != -1:
                dp[i] = dp[3] + dp[i-3]
                # print(i,"3먼저",dp)
            elif dp[i-5] == -1 and dp[i-3] == -1:
                dp[i] = -1
                # print(-1,"3먼저",dp)            
            else:
                dp[i] = dp[5] + dp[i-5]
                # print(i,"5먼저",dp)
    print(dp[n])
    

# f(1) = -1
# f(2) = -1
# f(3) = 1
# f(4) = -1
# f(5) = 1
# f(6) = 2  = f(3) + f(3)
# f(7) = -1  
# f(8) = 2  = f(5) + f(3)
# f(9) = 3  = f(3) + f(6)
# f(10) = 2 = f(5) + f(5)
# f(11) = 3 = f(5) + f(6)
# f(12) = 4 = f(3) + f(9)
# f(13) = 3 = f(3) + f(10)
# f(14) = 4 = f(5) + f(9)
