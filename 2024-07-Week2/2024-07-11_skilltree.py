"""
https://school.programmers.co.kr/learn/courses/30/lessons/49993
"""

def solution(skill, skill_trees):
    pos_st = [skill[:i] for i in range(len(skill)+1)]
    
    answer = 0
    for skills in skill_trees:
        tmp = ""
        for sk in skills:
            if sk in skill:
                tmp += sk
        
        if tmp in pos_st:
            answer += 1
            # print(tmp)
    return answer
