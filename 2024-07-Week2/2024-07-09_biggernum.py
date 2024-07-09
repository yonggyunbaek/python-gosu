"""
https://school.programmers.co.kr/learn/courses/30/lessons/154539
"""


# O(n^2) 시간초과
def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    # print(answer)
    for i in range(n):
        for j in range(i+1,n):
            if numbers[i] < numbers[j]:
                answer[i] = numbers[j]
                break
    # print(answer)
    return answer

# O(n) 통과
def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    return answer
