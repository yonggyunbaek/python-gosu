# https://school.programmers.co.kr/learn/courses/30/lessons/12899#

def solution(n):
    answer = ''
    while n > 0:
        n -= 1
        remain = n % 3
        num_dict = {0: '1', 1: '2', 2: '4'}
        answer += num_dict[remain]
        n //= 3

    return answer[::-1]
