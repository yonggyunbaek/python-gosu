# https://school.programmers.co.kr/learn/courses/30/lessons/134240

def solution(food):
    answer = ''
    
    for f in range(1,len(food)):
        answer += str(f) * (food[f] // 2)
    r_answer = answer[::-1]
    answer += '0'
    answer += r_answer
    return answer
