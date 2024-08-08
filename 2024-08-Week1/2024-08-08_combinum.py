# https://school.programmers.co.kr/learn/courses/30/lessons/68644

from itertools import combinations
def solution(numbers):
    answer = []
    combi_num = list(combinations(numbers,2))
    # print(combi_num)
    for n in combi_num:
        answer.append(sum(n))
    answer = list(set(answer))
    answer.sort()
    return answer
