"""
https://school.programmers.co.kr/learn/courses/30/lessons/12931
"""


def solution(n):
    answer = 0
    
    for num in str(n):
        answer += int(num)

    return answer
