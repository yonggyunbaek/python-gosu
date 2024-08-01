def solution(phone_number):
    answer = ''
    phone_number_len = len(phone_number)
    answer = '*' * (len(phone_number) - 4) + phone_number[-4:]
    
    return answer
