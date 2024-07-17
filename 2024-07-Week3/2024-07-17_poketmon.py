#https://school.programmers.co.kr/learn/courses/30/lessons/1845


def solution(nums):
    pick_num = len(nums)/2
    
    nums_set = set(nums)
    if len(nums_set) > pick_num:
        return pick_num
    else:
        return len(nums_set)