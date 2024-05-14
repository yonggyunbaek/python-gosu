# https://www.acmicpc.net/problem/14501
# dynamic programming

import sys
input = sys.stdin.readline

N = int(input())

schedule =  [ list(map(int, input().split())) for _ in range(N) ]
# dp의 각 원소는 인덱스 날짜까지 일을 했을 때 최대값
dp = [ 0 for _ in range(N+1) ] # N+1일은 퇴사일을 넘으니까 최대 보수는 0, N일은 N+1일을 참조함

# 역순으로 
for i in range(N-1, -1, -1):
    # 다음 번 날짜(인덱스)가 리스트 범위 벗어나면 현재 상태 유지
    if i + schedule[i][0] > N:
        dp[i] = dp[i+1]
    # 다음 번 날짜(인덱스)가 리스트 범위 안벗어나면
    else:
        # i번째날까지 일했을 때 최대값 = max(현재 까지 보수, i번째 날의 보수 + i부터 다음 인덱스 날에서 가질 수 있는 최대보수)
        dp[i] = max(dp[i+1], schedule[i][1] + dp[i+schedule[i][0]])
    # print(i, schedule[i], dp)
print(dp[0])



    