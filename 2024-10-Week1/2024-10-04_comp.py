# https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    n = len(s)
    min_length = n

    for unit in range(1, n // 2 + 1):
        compressed = ""
        count = 1
        prev = s[:unit]
        
        for i in range(unit, n, unit):
            if s[i:i + unit] == prev:
                count += 1
            else:
                compressed += (str(count) if count > 1 else "") + prev
                prev = s[i:i + unit]
                count = 1

        compressed += (str(count) if count > 1 else "") + prev

        min_length = min(min_length, len(compressed))

    return min_length
