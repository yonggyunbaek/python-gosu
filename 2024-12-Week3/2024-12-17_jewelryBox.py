# https://www.acmicpc.net/problem/2792

import sys
input = sys.stdin.readline

def bs(k:list, n:int):
    start, end = 1, max(k)
    result = 0
    while start <= end:
        cnt = 0
        mid = (start + end) // 2
        for i in k:
            if i%mid == 0:
                cnt += ( i//mid )
            else:
                cnt += ( i//mid +1 )
        if cnt > n:
            start = mid + 1
        else:
            result = mid
            end = mid - 1
    return result
    

n, m = map(int,input().split())
k = [ int(input()) for _ in range(m) ]


print(bs(k,n))