# https://school.programmers.co.kr/learn/courses/30/lessons/77484#

def solution(lottos, win_nums):
    answer = []
    zero=lottos.count(0)

    cnt=0
    for num in lottos:
        if num in win_nums:
            cnt+=1
            
    max_cnt=cnt+zero
    min_cnt=cnt

    max_place=7-max_cnt
    min_place=7-min_cnt
    
    if max_place>5:
        max_place=6
    if min_place>5:
        min_place=6
    
    
    
    answer.append(max_place)
    answer.append(min_place)

    return answer
