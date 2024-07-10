"""
https://school.programmers.co.kr/learn/courses/30/lessons/12912
"""

def solution(a, b):
    answer = 0
    if a > b:
        a, b = b, a
    for n in range(a,b+1):
        answer += n
    
    return answer
