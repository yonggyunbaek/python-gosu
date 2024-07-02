"""
https://school.programmers.co.kr/learn/courses/30/lessons/92335
"""

def convert(number, system):
    NUMBERS="0123456789"
    convert_num=""
    while number > 0:
        number, mod = divmod(number, system)
        convert_num += NUMBERS[mod]
    return convert_num[::-1]

def is_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False    
    return True


def solution(n, k):
    answer = 0
    tmp = convert(n,k).split('0')
    
    for t in tmp:
        if t == '' or t == '1':
            continue
            
        if is_prime_number(int(t)):
            answer += 1
    return answer
