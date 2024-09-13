# https://www.acmicpc.net/problem/12789

import sys
from collections import deque
input = sys.stdin.readline


def doki(students, stack):
# 1 ~ n까지 찾자
    for i in range(1,n+1):
        while students or stack:
            if students and students[0] == i:
                students.popleft()
                break
            elif stack and stack[-1] == i:
                stack.pop()
                break
            elif students:
                stack.append(students.popleft())
            else:
                return "Sad"
    if not students and not stack:
        return ("Nice")
    

n = int(input())
students = deque(map(int, input().split()))
stack = deque()
print(doki(students, stack))