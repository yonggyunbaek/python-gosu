# https://www.acmicpc.net/problem/10972

import sys

input = sys.stdin.readline

n = int(input())
p = list(map(int,input().split()))

find = False

# 뒤에서부터 확인 현재원소보다 큰 값이 나올때 까지
for i in range(n-1, 0, -1):
    # 한칸 앞 원소가 현재 원소보다 작으면
    if p[i-1] < p[i]:
        # 다시 맨 뒤 부터 큰값 찾기
        for j in range(n-1, 0, -1):
            if p[i-1] < p[j]:
                # 찾으면 값 교체
                p[i-1], p[j] = p[j], p[i-1]
                # p[i-1] 뒷 부분 정렬
                p = p[:i] + sorted(p[i:])
                find = True
                break
    if find:
        break
    
if find:
    print(*p)
else:
    print(-1)
