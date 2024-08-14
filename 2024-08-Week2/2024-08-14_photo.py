# https://school.programmers.co.kr/learn/courses/30/lessons/176963

from collections import defaultdict
def solution(name, yearning, photo):
    answer = []
    yearning_dict = defaultdict(int)
    for n, y in zip(name, yearning):
        yearning_dict[n] = y
    
    for cur_photo in photo:
        cur_score = 0
        for n in cur_photo:
            cur_score += yearning_dict[n]
        answer.append(cur_score)
    return answer
