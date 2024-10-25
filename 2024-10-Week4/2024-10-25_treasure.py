# https://www.acmicpc.net/problem/1026

import sys
input = sys.stdin.readline

n = int(input())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())),reverse=True)
answer = 0
for i in range(n):
    answer += A[i]*B[i]
print(answer)


# a.sort() 는 실행결과가 반영되는 inplace 함수
# sorted는 반환값으로 정렬된 결과를 주는 형태의 함수
# timsort 알고리즘 시간복잡도는 nlogn