# https://school.programmers.co.kr/learn/courses/30/lessons/42840

from math import ceil
def solution(answers):
    s1 = '12345' * ceil(len(answers) / 5)
    s2 = '21232425' * ceil(len(answers) / 7)
    s3 = '3311224455' * ceil(len(answers) / 9)
    student_rate = {
        '1' : 0,
        '2' : 0,
        '3' : 0
    }

    for index, a in enumerate(answers):
        if a == int(s1[index]):
            student_rate['1'] += 1
            # print(a,s1[index])
        if a == int(s2[index]):
            student_rate['2'] += 1
        if a == int(s3[index]):
            student_rate['3'] += 1
    
    answer = [int(k) for k,v in student_rate.items() if max(student_rate.values()) == v]
    # print(answer)
    if len(answer) == 0:
        return []
    else:
        return answer
