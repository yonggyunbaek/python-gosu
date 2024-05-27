# https://www.acmicpc.net/problem/1010

# 시간초과
# import sys
# from itertools import combinations

# input = sys.stdin.readline

# T = int(input())
# for _ in range(T):
#     N, M = map(int,input().split())
#     print(len(list(combinations(range(M),N)))) 
# 모든 조합을 생성하고 리스트로 변환
# 리스트로 저장해서 메모리 사용량 큼


import sys

input = sys.stdin.readline

def factorial(n):
    num = 1
    for i in range(1,n+1):
        num *= i
    return num

T = int(input())
for _ in range(T):
    N, M = map(int,input().split())
    answer = factorial(M) // (factorial(N) * factorial(M-N))
    print(answer)

# factorial(M)의 시간복잡도는 O(M)
# O(M) + O(N) + O(M - N) = O(M) -- 가장 큰 항만 고려