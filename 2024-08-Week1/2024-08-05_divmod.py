# https://school.programmers.co.kr/learn/courses/30/lessons/68935
def solution(n):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, 3)
        rev_base += str(mod)
    
    # print(rev_base)# 역순으로 나옴
    
    return int(rev_base,3)
