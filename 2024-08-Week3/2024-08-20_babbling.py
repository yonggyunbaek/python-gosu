# https://school.programmers.co.kr/learn/courses/30/lessons/133499

def solution(babbling):
    answer = 0
    status = False
    words = ["aya", "ye", "woo", "ma"]
    
    for b in babbling:
        tmp = 0
        before_word = ""
        while tmp < len(b):
            if b[tmp:tmp+3] in words and b[tmp:tmp+3] != before_word:
                before_word = b[tmp:tmp+3]
                tmp += 3
            elif b[tmp:tmp+2] in words and b[tmp:tmp+2] != before_word:
                before_word = b[tmp:tmp+2]
                tmp += 2
            else:
                status = False
                break
            status = True

        if status:
            answer += 1
    return answer
