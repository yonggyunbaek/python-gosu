#https://school.programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    n = sorted(list(str(n)), reverse=True)
    # print(n)
    return int(''.join(n))
