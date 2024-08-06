#https://school.programmers.co.kr/learn/courses/30/lessons/147355

def solution(t, p):
    answer = 0
    l = len(p)
    s = 0
    while s + l <= len(t):
        if int(t[s:s+l]) <= int(p):
            answer += 1
        s += 1
    return answer
