# 알파벳 문자열을 암호화
# 알파벳으로 된 문자열인 key
# 두 글자 단위로 암호화를 진행 

import sys
import copy
input = sys.stdin.readline

message = list(input().strip().upper())
modify_msg = []
cnt = 0
# print(message)
# 메시지 쌍 규칙
while len(message) != 0:
    m1 = message.pop(0)
    if len(message) == 0:
        modify_msg.append([m1,'X'])
        break
    else:
        m2 = message.pop(0)
        if m1 == m2 and m1 != 'X':
            modify_msg.append([m1,'X'])
            message.insert(0,m2)
        elif m1 == m2 and m1 == 'X':
            modify_msg.append([m1,'Q'])
            message.insert(0,m2)
        else:
            modify_msg.append([m1,m2])


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
        # for j in [xj, yj]:
        #     if j < 4:
        #         answer.append(key[xi][j+1])            
        #     elif j == 4:
        #         answer.append(key[xi][0])
        xj = (xj + 1) % 5
        yj = (yj + 1) % 5
        answer.append(key[xi][xj])
        answer.append(key[yi][yj])

    elif xj == yj: # 같은 열이면
        # for i in [xi, yi]:
        #     if i < 4:
        #         answer.append(key[i+1][xj])
        #     elif i == 4:
        #         answer.append(key[0][xj])
        xi = (xi + 1) % 5
        yi = (yi + 1) % 5
        answer.append(key[xi][xj])
        answer.append(key[yi][yj])
    else:
        answer.append(key[xi][yj])
        answer.append(key[yi][xj])

# print(answer, len(answer))
print(''.join(answer))