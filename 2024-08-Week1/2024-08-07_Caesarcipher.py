# https://school.programmers.co.kr/learn/courses/30/lessons/12926#

def solution(s, n):
    # print(ord("a"),ord("z"), ord("A"), ord("Z"))
    # print(chr(97),chr(122),chr(65),chr(90))
    # 97 122 65 90
    answer = ''
    if len(s) == 0:
        return ''
    
    for char in s:
        if char == ' ':
            answer += ' '
            continue
        if ord(char) >= 65 and ord(char) <= 90:# 대문자
            if ord(char) + n > 90:
                cur_char = chr(ord(char) + n - 26)
            else:
                cur_char = chr(ord(char) + n)
        if ord(char) >= 97 and ord(char) <= 122:# 소문자
            if ord(char) + n > 122:
                cur_char = chr(ord(char) + n - 26)
            else:
                cur_char = chr(ord(char) + n)
        answer += cur_char
    return answer
