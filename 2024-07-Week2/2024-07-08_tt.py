"""
https://school.programmers.co.kr/learn/courses/30/lessons/132265
"""

def solution(topping):
    answer = 0
    n = len(topping)
    
    # 오른쪽 토핑의 개수 저장
    right_count = {}
    for t in topping:
        right_count[t] = right_count.get(t, 0) + 1
    print(right_count)
    # 왼쪽 토핑의 개수 저장
    left_count = {}
    left = 0
    for right in range(n):
        left_count[topping[right]] = left_count.get(topping[right], 0) + 1
        right_count[topping[right]] -= 1
        if right_count[topping[right]] == 0:
            del right_count[topping[right]]
        if len(left_count) == len(right_count):
            print(left_count,right_count)
            answer += 1
    
    return answer
