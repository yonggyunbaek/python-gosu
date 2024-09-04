# https://school.programmers.co.kr/learn/courses/30/lessons/42746

def solution(numbers):
    str_numbers = list(map(str, numbers))
    str_numbers.sort(key=lambda x: x * 10, reverse=True)
    answer=''.join(str_numbers)
    return answer if answer[0]!= '0' else '0'
