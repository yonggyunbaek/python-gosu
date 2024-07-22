# https://school.programmers.co.kr/learn/courses/30/lessons/12906

from collections import deque
def solution(arr):
    arr = deque(arr)
    answer = []
    while arr:
        a = arr.popleft()
        if len(answer) == 0:
            answer.append(a)
        if a == answer[-1]:
            continue
        else:
            answer.append(a)
    return answer
