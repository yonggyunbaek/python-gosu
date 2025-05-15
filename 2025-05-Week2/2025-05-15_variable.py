# https://www.acmicpc.net/problem/16205

import re
import sys
input = sys.stdin.readline


def camel_to_snake(name):
    # 대문자 앞에 _를 붙이고 전체를 소문자로 변환
    # (?<!^): 문자열 시작이 아닌 위치에서
    # (?=[A-Z]): 대문자 앞에
    return re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()

def snake_to_camel(name):
    parts = name.split("_")
    return parts[0] + ''.join(w.capitalize() for w in parts[1:])

n, v = input().split()

if n == '1':
    print(v)
    print(camel_to_snake(v))
    print(v[0].upper()+v[1:])

elif n == '2':
    print(snake_to_camel(v))
    print(v)
    v = snake_to_camel(v)
    print(v[0].upper()+v[1:])
else:
    print(v[0].lower()+v[1:])
    v = v[0].lower()+v[1:]
    print(camel_to_snake(v))
    print(v[0].upper()+v[1:])