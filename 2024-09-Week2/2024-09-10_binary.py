# https://school.programmers.co.kr/learn/courses/30/lessons/77885

def to_binary_string(n):
    return "0" + bin(n)[2:]

def to_decimal(s):
    return int(s, 2)

def solution(numbers):
    answer = []
    for n in numbers:
        binary = to_binary_string(n)
        if binary[-1] == '0':
            answer.append(n+1)
            continue

        index = binary.rfind('01')
        if index != -1:
            new_binary = binary[:index] + '10' + binary[index + 2:]
            answer.append(to_decimal(new_binary))
        else:
            answer.append(n + 1)
    
    return answer


#시간 초과
# def solution(numbers):
#     answer = []
#     for n in numbers:
#         x = n
#         while n <= 10**15:
#             n += 1
#             if bin(x ^ n)[2:].count("1") <= 2:
#                 break        
#         answer.append(n)
#.    return answer