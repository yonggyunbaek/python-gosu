# https://school.programmers.co.kr/learn/courses/30/lessons/135808

def solution(k, m, score):
    answer = 0
    sorted_score = sorted(score,reverse=True)

    start, end = 0, m    
    while True:
        if end > len(sorted_score):
            break
        else:
            s_apple = sorted_score[start:end]
            answer += s_apple[-1]*m

        start += m
        end += m
    return answer
