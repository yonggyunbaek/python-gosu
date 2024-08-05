# https://school.programmers.co.kr/learn/courses/30/lessons/12982?language=python3
def solution(d, budget):        
    d.sort() # 오름차순 정렬
    
    cnt = 0
    for d_budget in d:        
        if budget - d_budget > 0:
            cnt += 1
            budget -= d_budget
            continue
        elif budget - d_budget == 0:
            cnt += 1
            return cnt
        else:
            return cnt
    return len(d)
