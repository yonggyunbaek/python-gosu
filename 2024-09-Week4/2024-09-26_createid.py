# https://school.programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    # 1. 소문자로 변환
    new_id = new_id.lower()
    
    # 2. 유효한 문자만 남기기
    valid_chars = []
    for char in new_id:
        if char.isalnum() or char in ['-', '_', '.']:
            if char == '.':
                if valid_chars and valid_chars[-1] != '.':
                    valid_chars.append(char)
            else:
                valid_chars.append(char)
    
    # 3. 문자열의 시작과 끝에 '.' 제거
    if valid_chars and valid_chars[0] == '.':
        valid_chars.pop(0)
    if valid_chars and valid_chars[-1] == '.':
        valid_chars.pop()
    
    # 4. 빈 문자열일 경우 'a'로 설정
    if not valid_chars:
        valid_chars.append('a')
    
    # 5. 길이가 16자 이상일 경우 15자까지 자르고, 끝에 '.'가 있으면 제거
    answer = ''.join(valid_chars)
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    
    # 6. 길이가 2자 이하일 경우 마지막 문자를 반복하여 길이 3으로 맞추기
    while len(answer) < 3:
        answer += answer[-1]
    
    return answer