# N개 컴퓨터 
# 예산 B 원
# 성능 리스트
# 성능 d만큼 증가시키는데 d^2 원
import sys

input = sys.stdin.readline

N, B = map(int, input().split())
performance = list(map(int, input().split()))

def check(check_num):
    cost = 0
    for p in performance:
        if p < check_num:
            cost += (check_num - p) ** 2
    return cost
   
start = 1
end = 2*10**9

def bsearch(start, end):
    if start == end:
        return start
    mid = (start + end + 1) // 2
    if check(mid) <= B:
        return bsearch(mid, end)
    else:
        return bsearch(start, mid - 1)

answer = bsearch(start,end)
print(answer)