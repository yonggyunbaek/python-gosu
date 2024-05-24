# https://www.acmicpc.net/problem/2493

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
q = list(map(int, input().split()))

# for i in range(N):
#     if i == 0:
#         print(0, end=" ")
#     else:
#         for j in range(i-1, -1, -1):
#             # print("i,j",i,j)
#             if q[j] > q[i]:
#                 print(j+1, end=" ")
#                 break
#             else:
#                 if j == 0:
#                     print(0, end=" ")

stack = []
answer = [0 for i in range(N)]

for i in range(N):
    while stack:
        # 스택에 제일 나중에 추가된 탑높이가 다음번 탑 높이보다 높다면
        if stack[-1][1] > q[i]:
            print("+1",stack)
            answer[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
        print("+1 or pop",stack)
    # 스택에 인덱스랑 탑높이 추가
    stack.append([i, q[i]])
    print(stack, answer)

print(*answer)