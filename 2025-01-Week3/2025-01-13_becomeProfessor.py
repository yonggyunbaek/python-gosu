# https://www.acmicpc.net/problem/3474

import sys
input = sys.stdin.readline

def cnt(n, answer):
    if n // 5 != 0:
        answer += (n // 5)
        return cnt(n // 5, answer)
    else:
        return answer

t = int(input())    
for _ in range(t):
    answer = 0    
    n = int(input())    
    print(cnt(n, answer))