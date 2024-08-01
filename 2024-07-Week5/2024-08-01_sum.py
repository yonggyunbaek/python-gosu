def solution(numbers):
    # answer = [1,2,3,4,5,6,7,8,9]
    answer = [n for n in range(10)]
    sum_answer, sum_numbers = sum(answer), sum(numbers)
    
    return sum_answer - sum_numbers
