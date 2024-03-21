"""
문제
남우는 어버이날을 맞아 부모님의 일을 돕기로 하였습니다. 남우의 부모님께서는 농사를 지으시기에, 남우는 땅을 일구는 일을 도우려고 합니다.

남우에게 할당된 땅은 3* 3 크기의 격자로 이루어져 있으며, 각 땅의 높이는 1이상 3이하의 정수값으로 이루어져 있습니다. 부모님께서 농사를 지을 땅의 크기는 1*3이며, 농사를 짓기 위해서는 해당 영역 내 땅의 높이가 전부 동일해야 합니다. 따라서 남우는 특정 땅의 높이를 낯추거나 높여, 3 * 3 격자 내에 부모님께서 농사를 지을 수
있는 영역이 최소 1곳 이상 생기도록 만들려고 합니다.

남우가 특정 땅의 높이를 1만큼 낯추거나 높이는데 1만큼의 비용이 소요된다고 했을 때, 부모님께서 농사를 지으실 수 있도록 땅을 일구기 위해 남우에게 필요한 최소 비용을 구하는 프로그램을 작성해보세요.
단, 1* 3크기의 영역은 가로, 세로로 놓이는 것이 모두 가능하기에, 3 * 3 크기의 격자에서는 땅의 높이만 동일하다면 최대 6개의 영역에 농사를 지을 수 있음에 유의합니다.

제약조건
• 1s 땅의 높이 ≤ 3

입력형식
세 개의 졸에 걸쳐 각 행에 해당하는 땅의 높이 정보가 공백을 사이에 두고 주어집니다.

출력형식
부모님께서 농사를 짓는 것이 가능해지기 위해 남우에게 필요한 최소 비용을 출력합니다.
"""

import sys

land = [list(map(int,sys.stdin.readline().split())) for _ in range(3)]
# print(land)

# 가로 체크
min_cost = 2
for a,b,c in land:
    # print(a,b,c)
    if a == b == c:
        cost = 0
    elif a != b == c:
        cost = abs(a-b)
    elif a == b != c:
        cost = abs(b-c)
    elif a != c == b:
        cost = abs(a-c)
    else:
        cost = 1
    min_cost=min(min_cost,cost)
# 세로 체크

for column in range(3):
    a, b, c = land[0][column], land[1][column], land[2][column]
    if a == b == c:
        cost = 0
    elif a != b == c:
        cost = abs(a-b)
    elif a == b != c:
        cost = abs(b-c)
    elif a != c == b:
        cost = abs(a-c)
    else:
        cost = 1
    min_cost=min(min_cost,cost)

print(min_cost)