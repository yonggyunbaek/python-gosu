
# 백준 1920

import sys

input = sys.stdin.readline

N = int(input().strip())
A = list(map(int, input().split()))
M = int(input().strip())
Mlist = list(map(int, input().split()))
A.sort()


def binary_search(target, A, start, end):
    if start > end:
        return 0
    
    middle = (start + end) // 2
    if target == A[middle]:
        return 1
    elif target < A[middle]:
        return binary_search(target, A, start, middle-1)
    else:
        return binary_search(target, A, middle+1, end)
    
for k in Mlist:
    start = 0
    end = N - 1
    print(binary_search(k, A, start, end))




