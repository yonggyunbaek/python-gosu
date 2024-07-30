def solution(x, n):
    answer = []
    s = 0
    for _ in range(n):
        s += x
        answer.append(s)
    return answer