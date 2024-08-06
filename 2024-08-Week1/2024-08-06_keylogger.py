# https://www.acmicpc.net/problem/5397

# 인덱스를 +,- 하면서 리스트에 insert 하면 시간초과
# 좌우 deque를 만들어 놓고 마지막에 합치기

import sys
from collections import deque
input = sys.stdin.readline

def logger(password: str) -> str:
    left = deque()
    right = deque()
    
    for char in password:
        if char == "<":
            if left:
                right.appendleft(left.pop())
        elif char == ">":
            if right:
                left.append(right.popleft())
        elif char == "-":
            if left:
                left.pop()
        else:
            left.append(char)
        print(char,left,right)

    # 결과 문자열을 얻기 위해 두 deque를 합침
    return ''.join(left) + ''.join(right)

n = int(input())
for _ in range(n):
    password = input().rstrip()
    print(logger(password))
