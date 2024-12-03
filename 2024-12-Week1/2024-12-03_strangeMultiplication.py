# https://www.acmicpc.net/problem/1225

import sys
input = sys.stdin.readline

A, B = input().split()

# 시간초과
# for i in list(A):
#     for j in list(B):
#         answer += int(i) * int(j)
    
# 123 45
# 1*4 + 1*5 + 2*4 + 2*5 + 3*4 + 3*5 = 1(4+5) + 2(4+5) + 3(4+5) = (1+2+3)(4+5)
# 각자리수 합쳐서 곱

print( sum( int(i) for i in A ) * sum(int(i) for i in B) )
