# https://www.acmicpc.net/problem/1769

import sys
input = sys.stdin.readline

def mot(numstring: str, cnt: int) -> str:
    if len(numstring) == 1:
        return numstring, cnt
    
    n = list(numstring)
    s = sum( int(i) for i in n)
    v = str(s)
    cnt += 1
    if len(v) == 1:
        return v, cnt
    
    return mot(v, cnt)


X = input().strip()
answer, cnt = mot(X, 0)
if int(answer) % 3 == 0:
    print(cnt)
    print("YES")
else:
    print(cnt)
    print("NO")