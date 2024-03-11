"""
문제

루팡은 배낭을 하나 메고 은행금고에 들어왔다. 금고 안에는 값비싼 금, 은, 백금 등의 귀금속 덩어리가 잔뜩 들어있다. 배낭은 W kg까지 담을 수 있다.
각 금속의 무게와 무게당 가격이 주어졌을 때 배낭을 채울 수 있는 가장 값비싼 가격은 얼마인가?
루팡은 전동톱을 가지고 있으며 귀금속은 톱으로 자르면 잘려진 부분의 무게만큼 가치를 가진다.

제약조건
1≤N≤ 106인 정수
1≤W≤ 104인 정수
1≤ M, P1 ≤ 104인 정수

입력형식
첫 번째 줄에 배낭의 무게 W와 귀금속의 종류 N이 주어진다. i+ 1 (1≤i≤ N)번째 줄에는 i번째 금속의 무게 M,와 무게당 가격 P,가 주어진다.

출력형식
첫 번째 줄에 배낭에 담을 수 있는 가장 비싼 가격을 출력하라.
"""

import sys

W, N = map(int, sys.stdin.readline().split())
metal = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


# metal.sort(key=lambda x: (-x[1], x[0]))
metal.sort(key = lambda x : x[1], reverse = True)
total_weight, total_price = 0, 0
for weight, price in metal:
    if total_weight + weight <= W:
        total_weight += weight
        total_price += weight * price
        if total_weight == W:
            break
    else:
        remain_weight = W - total_weight  # 남은 무게를 계산합니다.
        total_price += remain_weight * price
        break

print(total_price)
