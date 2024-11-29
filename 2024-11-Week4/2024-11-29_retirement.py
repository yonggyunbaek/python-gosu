# https://e-room.tistory.com/200

import sys
input = sys.stdin.readline

# index에 해당하는 원하는 값(최대 수익) 구하는 함수
def sol(index:int) -> int:
    if index == n:
        return 0
    if index > n:
        return -1e9
    if dp[index] != -1:
        return dp[index]
    dp[index] = max(sol(index + schedule[index][0]) + schedule[index][1], sol(index+1))
    print(dp)
    return dp[index]
    

n = int(input())
schedule = [ list(map(int, input().split())) for _ in range(n) ]
dp = [-1] * n

print(sol(0))
