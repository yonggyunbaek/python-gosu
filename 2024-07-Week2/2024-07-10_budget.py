# https://www.acmicpc.net/problem/2512

import sys
input = sys.stdin.readline

N = int(input())
budget = list(map(int,input().split()))
M = int(input())

start = 1
end = max(budget)

# 특정 상한액을 찾아야함
# start, end 로 중간값 확인해서 예산(money)를 계산해보고 
# 예산을 안넘으면 start를 중간값+1 로 바꾸고 다시 중간값 계산해서 예산 확인
# 예산을 넘으면 end를 중간값-1 로 바꾸고 다시 중간값 계산해서 예산 확인
# start가 end 보다 커지면 중단

while start <= end:
    mid = (start + end) // 2
    money = 0
    for i in budget:
        # 요소가 중간값보다 크면
        if i - mid > 0:
            # 중간값 추가
            money += mid
        # 요소가 중간값보다 작으면
        else:
            # 요소값 추가
            money += i
    
    if money <= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)