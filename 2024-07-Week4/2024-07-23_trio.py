#

from itertools import combinations
def solution(number):
    
    answer = list(combinations(number,3))
    result = 0
    for a in answer:
        # print(a)
        # print(sum(a))
        if sum(a) == 0:
            result += 1


    return result


