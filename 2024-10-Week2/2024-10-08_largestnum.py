# https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(number, k):
    stack = []

    for i in range(len(number)):
        while k > 0 and stack and stack[-1] < number[i]:
            stack.pop()
            k -= 1
        stack.append(number[i])
    

    if k > 0:
        stack = stack[:-k]
    

    return ''.join(stack)
