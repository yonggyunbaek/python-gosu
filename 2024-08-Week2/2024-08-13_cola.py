# https://school.programmers.co.kr/learn/courses/30/lessons/132267#

def solution(a, b, n):
    answer = 0
    while n // a > 0:
        change_cola, remain_cola = divmod(n, a)
        answer += change_cola * b
        
        n = change_cola * b + remain_cola
    return answer
