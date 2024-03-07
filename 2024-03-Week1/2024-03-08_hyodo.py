"""
문제

남우는 m명의 친구를 불러 나무에서 열매를 수확하는 일을 맡겼습니다. 나무들은 n * n 크기의 격자 모양의 땅 위의 모든 칸에 심어져 있고, 각 나무마다 가능한 열매 수확량이 주어져 있습니다.

친구들은 n * n 크기의 격자 내의 서로 다른 위치에서 출발하여 1초에 1칸씩 상하좌우 인접한 칸 중 한 곳으로 움직일 수 있으며, 최종적으로 모든 열매 수확량의 합을 최대로 만들고자 합니다. 이때 각 칸에서 열매를 수확하는데 걸리는 시간은 0초이며,
한 나무에 여러 친구가 방문하게 되더라도 열매는 딱 한 번만 수확이 가능합니다. 또, 친구들끼리 이동하는 도중 만나게 되는 것 역시 가능합니다.

m명의 친구들이 3초 동안 최대로 얻을 수 있는 열매 수확량의 총 합을 구하는 프로그램을 작성해보세요.

본 문제의 저작권은 (주)브랜치앤바운드에 있으며, 저작자의 동의 없이 무단 전재/복제/배포를 금지합니다.

제약조건

[조건 1] 2≤n≤20

[조건 2] 1≤m≤3

[조건 3] 1≤ 가능한 열매 수확량 ≤ 1,000

입력형식

첫 번째 줄에 n과 m이 공백을 사이에 두고 주어집니다.

두 번째 줄부터는 n개의 줄에 걸쳐 각 행에 해당하는 n개의 가능한 열매 수확량 정보가 공백을 사이에 두고 주어집니다.
n + 2번째 줄부터는 m개의 줄에 걸쳐 각 친구의 위치 정보 (X1, Y1)가 공백을 사이에 두고 주어집니다. 이는 친구가 (X, 행, Y1 열)에 위치해 있음을 뜻하며, 처음 위치가 겹쳐져 주어지는 경우는 없다고 가정해도 좋습니다.

출력형식

첫 번째 줄에 얻을 수 있는 최대 열매 수확량의 합을 출력하세요. 단, 처음 시작하는 칸의 경우 0초 때 열매 수확이 가능함에 유의합니다.

입력 예시 1

4.2.
20_26_185_80.
100_20_25_80.
20_20_88_99.
15.32.44.50.
1.2.
2.3

출력 예시 1

633

다음과 같이 움직이면 3초 안에 열매 수확량 총합 633을 얻을 수 있습니다.
"""

import sys
from itertools import product

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def is_valid(x, y):
    return 0 <= x < n and 0 <= y < n

def get_max_fruits(friends):
    temp_board = [board[i][:] for i in range(n)]
    total_fruits = 0
    for friend in friends:
        for x, y in friend:
            total_fruits += temp_board[x][y]
            temp_board[x][y] = 0
    return total_fruits

def dfs(lst, cnt):
    if cnt == time:
        friends[friend].append(lst[:])
        return
    for i in range(4):
        nx, ny = lst[-1][0] + dx[i], lst[-1][1] + dy[i]
        if is_valid(nx, ny):
            lst.append([nx, ny])
            dfs(lst, cnt+1)
            lst.pop()

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
start = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
time = 4
friends = [[] for _ in range(m)]
answer = 0

for friend in range(m):
    x, y = start[friend]
    x -= 1
    y -= 1
    dfs([[x, y]], 1)

for perm in product(*friends):
    answer = max(answer, get_max_fruits(perm))

print(answer)
