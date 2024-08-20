#https://school.programmers.co.kr/learn/courses/30/lessons/17682

import re
def solution(dartResult):
    answer = 0
    step = 0
    score = list(map(lambda x : int(x),re.findall('\d+', dartResult)))
    
    for d in dartResult:
        if d.isnumeric():
            continue
        elif d.isalpha():
            if d == "S":
                step += 1
                continue
            elif d == "D":
                score[step] = score[step] ** 2
                step += 1
            elif d == "T":
                score[step] = score[step] ** 3
                step += 1
        else:
            if d == "*":
                if step >= 2:
                    score[step-2] = score[step-2] * 2
                    score[step-1] = score[step-1] * 2
                else:
                    score[0] = score[0] * 2
            if d == "#":
                score[step-1] = score[step-1] * (-1)
    return sum(score)
