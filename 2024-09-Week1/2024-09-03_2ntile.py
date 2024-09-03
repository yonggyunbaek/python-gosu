# https://school.programmers.co.kr/learn/courses/30/lessons/12900

def solution(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    
    # 이전 두 값을 저장할 변수
    prev2 = 1  # dp[0]
    prev1 = 1  # dp[1]
    
    for i in range(2, n + 1):
        current = (prev1 + prev2) % 1000000007
        prev2 = prev1
        prev1 = current
    
    return prev1
