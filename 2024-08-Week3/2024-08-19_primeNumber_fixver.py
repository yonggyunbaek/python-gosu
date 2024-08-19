# https://school.programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations
import math

def solution(nums):
    answer = 0
    combi_nums = combinations(nums, 3)
        
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    for c_n in combi_nums:
        sum_n = sum(c_n)
        if is_prime(sum_n):
            answer += 1
            
    return answer
