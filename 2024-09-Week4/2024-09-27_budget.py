# https://www.acmicpc.net/problem/2512

import sys
input = sys.stdin.readline

# 입력 받기
n = int(input())  # 예산 요청의 수
arr = list(map(int, input().split()))  # 각 요청의 금액 리스트
M = int(input())  # 총 예산

# 이진 탐색을 위한 초기 값 설정
low = 0
high = max(arr)
result = 0

# 이진 탐색 시작
while low <= high:
    mid = (low + high) // 2  # 중간 값 (상한선)
    temp = 0  # 상한선을 기준으로 배정할 총 금액 계산

    # 각 요청에 대해 상한선을 넘는지 확인하고 예산 계산
    for i in arr:
        if i > mid:
            temp += mid  # 요청 금액이 상한선을 넘으면 상한선만큼만 더함
        else:
            temp += i  # 요청 금액이 상한선 이하이면 요청 금액 그대로 더함
    
    # 배정한 금액이 총 예산 M을 초과하는지 확인
    if temp <= M:
        result = mid  # 배정한 금액이 예산을 넘지 않으면 현재 상한선을 저장
        low = mid + 1  # 상한선을 더 높여도 되는지 확인하기 위해 low 값을 높임
    else:
        high = mid - 1  # 배정 금액이 예산을 넘으면 상한선을 낮춤
    
    # 디버깅용 출력 (필요 없으면 제거 가능)
    print(f"low: {low}, mid: {mid}, high: {high}, temp: {temp}")

# 최종 결과 출력
print(result)
