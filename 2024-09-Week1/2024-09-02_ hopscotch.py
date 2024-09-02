# https://school.programmers.co.kr/learn/courses/30/lessons/12913

def solution(land):
    #dynamic programming
    dp = [[0]*4 for _ in range(len(land))]
    # test = [except_i for except_i in range(4) if except_i != 1]
    for i in range(len(land)):# row
        for j in range(len(land[0])): # space
            if i == 0:
                dp[i][j] = land[i][j]
            else:
                dp[i][j] = land[i][j] + max(dp[i-1][except_i] for except_i in range(4) if except_i != j)            
    """
dp[i][0] = land[i][0] + max(dp[i-1][1], dp[i-1][2], dp[i-1][3])
dp[i][1] = land[i][1] + max(dp[i-1][0], dp[i-1][2], dp[i-1][3])
    """
    return max(dp[-1])
