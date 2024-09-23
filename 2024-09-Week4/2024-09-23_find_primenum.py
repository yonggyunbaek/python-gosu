#  https://school.programmers.co.kr/learn/courses/30/lessons/42839?language=python3

from itertools import permutations
from math import sqrt
def is_primenum(x):
    for i in range (2, int(sqrt(x)) + 1):
    	if x % i == 0:
        	return False
    return True

def solution(numbers):
    num_list = []
    answer = []
    for n in range(1, len(numbers)+1):
        num_list += permutations(numbers,n)
    num_list = list(set(num_list))
    # print(num_list)
    for num in num_list:
        tmp = int(''.join(num))
        if is_primenum(tmp):
            if tmp >= 2 and tmp not in answer:
                answer.append(tmp)
    return len(answer)
