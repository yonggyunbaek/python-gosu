"""
LZW 압축하기
https://school.programmers.co.kr/learn/courses/30/lessons/17684
"""

def solution(msg):
    answer = []
    # CHAR = {"A":1,"B":2,"C":3,"D":4,"E":5,
    #          "F":6,"G":7,"H":8,"I":9,"J":10,
    #          "K":11,"L":12,"M":13,"N":14,"O":15,
    #          "P":16,"Q":17,"R":18,"S":19,"T":20,
    #          "U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}
    CHAR = {chr(i + 64): i for i in range(1, 27)}
    
    cur_char, next_char = 0, 0
    while True:
        next_char += 1
        # 마지막 글자 추가
        if next_char == len(msg):	
            answer.append((CHAR[msg[cur_char:next_char]]))
            break
        
        # 단어 없으면 추가
        if msg[cur_char:next_char+1] not in CHAR:
            CHAR[msg[cur_char:next_char+1]] = len(CHAR) + 1
            answer.append(CHAR[msg[cur_char:next_char]])
            cur_char = next_char	 

    return answer
