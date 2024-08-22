# https://school.programmers.co.kr/learn/courses/30/lessons/155652

def solution(s, skip, index):
    for _ in range(index):
        tmp = ""
        for char in s:
            next_char = chr(ord(char) + 1)
            while next_char in skip or next_char > 'z':
                if next_char > 'z':
                    next_char = 'a'
                else:
                    next_char = chr(ord(next_char) + 1)
            
            tmp += next_char
        s = tmp
    return s
