# https://www.acmicpc.net/problem/13909

import sys
input = sys.stdin.readline


n = int(input())
# n의 약수는 홀수개여야 창문 열림 -> n은 어떤수의 제곱수
print( int(n**(1/2)) )

# 메모리 초과
# window = [ 0 for _ in range(n+1)]
# for i in range(1,n+1):
#     for j in range(1, n+1):
#         if i*j > n:
#             break
#         if window[i*j] == 0:
#             window[i*j] = 1
#         else:
#             window[i*j] = 0
    
# print(window[1:].count(1))