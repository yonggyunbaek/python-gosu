# https://www.acmicpc.net/problem/3190

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
k = int(input())

# 전체 그래프 0으로
graph = [ [0] * n for _ in range(n) ]

# 사과 위치 2로
for i in range(k):
    a, b = map(int,input().split())
    graph[a-1][b-1] = 2

l = int(input())
dirDict = {}
# x초 c방향정보 dict
for i in range(l):
    x, c = input().split()
    dirDict[int(x)] = c

# 방향표현
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# 뱀 위치 queue
q = deque()
q.append((0,0))

x, y = 0, 0
graph[x][y] = 1
cnt = 0
direction = 0

#direction은 dx,dy의 인덱스
def turn(c):
    global direction
    if c == 'L':
        direction = (direction -1) % 4
    else:
        direction = (direction +1) % 4

while True:
    # 시간 카운트
    cnt += 1
    x += dx[direction]
    y += dy[direction]
    #  벽 만나면 
    if x < 0 or x >= n or y < 0 or y >= n:
        break

    # 사과 만나면
    if graph[x][y] == 2:
        graph[x][y] = 1
        q.append((x,y))
        # 방향전환할 시간이면
        if cnt in dirDict:
            turn(dirDict[cnt])
    
    # 앞으로 전진
    elif graph[x][y] == 0:
        graph[x][y] = 1
        q.append((x,y))
        tx, ty = q.popleft()
        # 지나간 자리 0
        graph[tx][ty] = 0
        # 방향전환할 시간이면
        if cnt in dirDict:
            turn(dirDict[cnt])

    # 1을 만나면 = 길어진 몸 만나면
    else:
        break
print(cnt)