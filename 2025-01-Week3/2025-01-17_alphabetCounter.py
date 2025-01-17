import sys
# 길이 결과값을 저장할 리스트
result = [0]*26

# sys.stdin.read()를 통해 입력을 eof 날 때 까지 받을 수 있다.
s = sys.stdin.read().replace('\n', '').replace(' ','')

# result 리스트의 0번 인덱스(a)부터 해당 문자가 존재한다면 1씩 추가해준다.
# ord() 함수
# ord란 ordinal position의 약자로, 문자의 순서 위치 값을 의미한다.
# 10진수 유니코드(Unicode)로 값을 변환해준다.

for i in s:
    result[ord(i)-97] += 1

# chr() 함수
# chr이란 chracter의 약자로, 정수 값을 유니코드 문자로 변환한다.
# a = chr(97)
for j in range(26):
    # 만약 리스트의 인덱스가 최댓값과 같다면(최댓값이 여러개라면)
    if result[j] == max(result):
        # 문자를 알파벳 순서에 따라 출력한다.
        print(chr(97+j), end ='')