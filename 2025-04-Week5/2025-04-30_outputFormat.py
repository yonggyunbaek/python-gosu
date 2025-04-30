# https://www.acmicpc.net/problem/5177

import re
import sys
input = sys.stdin.readline

k = int(input())

for i in range(k):
    a = input().strip().replace("{","(").replace("}",")").replace("[","(").replace("]",")").replace(";",",").lower()
    b = input().strip().replace("{","(").replace("}",")").replace("[","(").replace("]",")").replace(";",",").lower()
    
    # sub 문자열 치환
    # re.sub(바꾸고 싶은 패턴, 무엇으로 바꿀지, 원래 문자열)
    # r: raw string을 뜻 \를 escape하지 않고 그대로 쓰도록
    # \s: 공백
    # {2,}: 바로 앞의 항목이 2번 이상 반복
    a = re.sub(r'\s{2,}', ' ', a)
    b = re.sub(r'\s{2,}', ' ', b)

    # \s* 공백 여러개
    # ([:(),.]) 바깥 ()는 캡처그룹, 안에 내용을 다시 사용할 수 있도록 기억
    # [...] 문자 클래스, 대괄호 안의 문자중 하나를 의미
    # 대괄호 안에는 매칭 대상 문자들
    # r'\1' 첫번째 캡처 그룹의 값, 캡처한 문자(기호)만 남기고 앞뒤 공백 제거
    a = re.sub(r'\s*([:(),.])\s*', r'\1', a)
    b = re.sub(r'\s*([:(),.])\s*', r'\1', b)

    if a == b:
        print("Data Set ",i+1,": equal", sep="")
        print()
    else:
        print("Data Set ",i+1,": not equal", sep="")
        print()