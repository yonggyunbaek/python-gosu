# https://www.acmicpc.net/problem/14244

import sys
input = sys.stdin.readline

n,m = map(int,input().split())

cnt = 0
for i in range(n-1):
    print(cnt,i+1)
    if n-m>cnt:
        cnt+=1

# 리프는 최소 2개  0-1-2-3 일 경우 0,3이 리프
# n개의 노드 m개의 리프
# n-m까지 직선노드를 증가시키고 나머지는 리프로 달아 준다
# n = 5, m = 3이면 n-m = 2 니까 0-1-2까지 직선노드 증가시키고 3,4는 2 밑으로 붙인다
# 예시 답
# 0 1
# 1 2
# 2 3
# 2 4
