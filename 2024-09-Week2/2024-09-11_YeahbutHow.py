# https://softeer.ai/practice/9498

import sys
from collections import deque
input = sys.stdin.readline

S = input().rstrip()
s = deque(S)
result = []
while s:
    result.append(s.popleft())
    if not s:
        break
    if result[-1] == "(" and s[0] ==")":
        result.append('1')
    elif result[-1] == ")" and s[0] =="(":
        result.append('+')
    
    # print(s, result)

print("".join(result))

# result를 문자열로 놓고 + 로 붙이는것 보다
# list에 append 하고 마지막에 join 하는게 시간복잡도가 더 효율적이다
# 문자열 += 를 이용할 경우 문자열의 immutability 때문에 + 할 때 마다 새로운 문자열이 생성된다
# 매번 새로운 문자열이 생성되고, 기존 문자열의 내용이 모두 새로 생성된 문자열로 복사된다 O(n^2)
