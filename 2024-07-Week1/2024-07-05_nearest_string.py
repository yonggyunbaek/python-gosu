"""
https://school.programmers.co.kr/learn/courses/30/lessons/142086
"""

def solution(s):
    answer = []
    check = {}
    for index, char in enumerate(s):
        if char not in check:
            answer.append(-1)
            check[char] = index
            continue
        else:
            loc = index - check[char]
            answer.append(loc)
            check[char] = index
        # print(index,char)
    return answer