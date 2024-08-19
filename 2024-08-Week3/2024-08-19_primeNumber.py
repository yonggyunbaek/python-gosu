#

from itertools import combinations
def solution(nums):
    answer = 0
    """
    3개의 nums의 element를 더해서 소수 만들기.
    prime number : 소수
    """
    # print(list(combinations([1,2,3],2)))
    
    combi_nums = list(combinations(nums,3))
    for c_n in combi_nums:
        count = 0
        sum_n = sum(c_n)
        for div_n in range(2,sum_n//2 + 1):
            if sum_n % div_n == 0:
                count += 1
        
        if count == 0:
            answer += 1
        else:
            continue
    return answer
