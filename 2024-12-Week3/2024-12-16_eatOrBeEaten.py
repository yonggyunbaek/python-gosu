# https://www.acmicpc.net/problem/7795

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    # print(a,b)
    cnt = 0
    j = 0 # b 인덱스

    for i in range(n):
        # 이중 포문으로 계속 처음부터 돌지 말고 정렬한 리스트니까 j 한칸씩 앞으로 가면서 반복횟수 줄이기
        while j < m and a[i] > b[j]:
            j += 1
        cnt += j
    print(cnt)