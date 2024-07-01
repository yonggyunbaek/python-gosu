"""
https://school.programmers.co.kr/learn/courses/30/lessons/17687
"""

# 1. convert num system
def convert(num, n): # n jinsu
    if num == 0:
        return 0
    NUMBERS="0123456789ABCDEF"
    convert_num=""
    while num > 0:
        num, mod = divmod(num, n)
        convert_num += NUMBERS[mod]
    return convert_num[::-1]

def solution(n, t, m, p):
    answer, num_list = [], []
    cur_num = p - 1
    
    for num in range(t*m):
        num_list.extend(str(convert(num, n)))
    while True:
        if len(answer) == t:
            break
        answer.append(num_list[cur_num])
        cur_num += m
    # print(answer)
    return ''.join(answer)