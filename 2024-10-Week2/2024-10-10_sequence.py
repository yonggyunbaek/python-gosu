# https://school.programmers.co.kr/learn/courses/30/lessons/178870

def solution(sequence, k):
    answer = []
    min_len = len(sequence)
    start, current_sum = 0, 0
    
    if k in sequence:
        return [sequence.index(k), sequence.index(k)]
    
    
    for end in range(len(sequence)):
        current_sum += sequence[end]

        while current_sum > k and start <= end:
            current_sum -= sequence[start]
            start += 1

        if current_sum == k:
            if (end - start) < min_len:
                min_len = end - start
                answer = [start, end]
    return answer
