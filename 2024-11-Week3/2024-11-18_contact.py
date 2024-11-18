# https://www.acmicpc.net/problem/1013

import re

pattern = r'^(100+1+|01)+$'

T = int(input())

for _ in range(T):
    signal = input().strip()
    
    # 패턴과 일치하는지 확인
    if re.match(pattern, signal):
        print("YES")
    else:
        print("NO")
