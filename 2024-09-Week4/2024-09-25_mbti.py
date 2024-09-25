# https://school.programmers.co.kr/learn/courses/30/lessons/118666?language=python3
def solution(survey, choices):
    answer = ''
    MBTI = {"RT":0,
            "CF":0,
            "JM":0,
            "AN":0
           }
    standard_type = ["RT", "CF", "JM", "AN"]
    for s, c in zip(survey, choices):
        c -= 4
        if s not in standard_type:
            s = s[::-1]
            c = -c
        
        if c == 0:
            continue
        elif c < 0:
            MBTI[s] += c
        else:
            MBTI[s] += c
    # print(MBTI)
    for k, v in MBTI.items():
        if v <= 0:
            answer += k[0]
        else:
            answer += k[1]
    return answer