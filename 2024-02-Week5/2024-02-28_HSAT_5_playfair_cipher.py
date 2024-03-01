# 알파벳 문자열을 암호화
# 알파벳으로 된 문자열인 key
# 두 글자 단위로 암호화를 진행 

import sys
import copy
input = sys.stdin.readline

message = list(input().strip())
modify_msg = copy.deepcopy(message)
cnt = 0

# 메시지 쌍 규칙
for i in range(len(message)):
    
    if i % 2 != 0: #인덱스 홀수, 리스트 짝수번째
        if message[i] == message[i-1]:
            if message[i-1] != 'X' and (i+cnt) % 2 == 1:
                modify_msg.insert(i+cnt,'X')
                cnt += 1
            elif message[i-1] == 'X' and (i+cnt) % 2 == 1:
                modify_msg.insert(i+cnt,'Q')
                cnt += 1
            else:
                continue
            # print('\ni',i,modify_msg)
    
if len(modify_msg) % 2 == 1:
    modify_msg.append('X')
modify_msg = [modify_msg[i:i+2] for i in range(0, len(modify_msg), 2)]
# print("\nmodify_msg", modify_msg, len(modify_msg))


# key입력받기
keystr = list(input().strip())
# dictionary는 키값을 넣는 순서를 기억한다. 리스트 중복을 제거하면서 순서 유지 가능
keystr = list(dict.fromkeys(keystr))

for i in range(ord('A'),ord('Z')+1):
    if chr(i) in keystr:
        continue
    elif chr(i) != 'J':
        keystr.append(chr(i))

# key 2차원 배열로 만들기

key = [keystr[i:i+5] for i in range(0, 25, 5)]
# print(key)
answer = []
for x,y in modify_msg: # 알파벳 쌍 
    for i in range(5): # 행
        if x in key[i]:
            xi = i
            xj = key[i].index(x)
        if y in key[i]:
            yi = i
            yj = key[i].index(y)

    if xi == yi: # 같은행이면
        for j in [xj, yj]:
            if j < 4:
                answer.append(key[xi][j+1])            
            elif j == 4:
                answer.append(key[xi][0])

    elif xj == yj: # 같은 열이면
        for i in [xi, yi]:
            if i < 4:
                answer.append(key[i+1][xj])
            elif i == 4:
                answer.append(key[0][xj])
    else:
        answer.append(key[xi][yj])
        answer.append(key[yi][xj])

# print(answer, len(answer))
print(''.join(answer))