# N개 컴퓨터 
# 예산 B 원
# 성능 리스트
# 성능 d만큼 증가시키는데 d^2 원
import sys

input = sys.stdin.readline

N, B = map(int, input().split())
performance = list(map(int, input().split()))

check_num = 1

while True:
    cost = 0
    for p in performance:
        if p < check_num:
            cost += (check_num - p) ** 2
            
    if cost < B:
        check_num += 1
        continue
    elif cost == B:
        print(check_num)
        break
    else:
        print(check_num - 1)
        break
    