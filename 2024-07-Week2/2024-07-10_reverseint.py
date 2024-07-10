"""
https://school.programmers.co.kr/learn/courses/30/lessons/12932
"""

def solution(n):
    return list(map(lambda x: int(x), str(n)[::-1]))
