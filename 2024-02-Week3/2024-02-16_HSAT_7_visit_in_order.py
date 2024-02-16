import sys

input = sys.stdin.readline

def dfs(now, destIdx):
    global cnt
    if now == dest[destIdx]:
        if destIdx == M-1:
            cnt += 1
            return
        else:
            destIdx += 1
    # 현재 좌표
    x, y = now
    # 방문 표시
    visited[x][y] = True
    # 상하좌우 4번
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        # grid 벗어나는거 확인 and 방문확인 and grid벽 확인
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False and grid[x][y] == 0:
            dfs([nx, ny], destIdx)
    # 
    visited[x][y] = False
    return


N, M = map(int,input().split())
grid = [ list(map(int,input().split())) for _ in range(N) ]
dest = []
for _ in range(M):
    x,y = map(int,input().split())
    dest.append([x-1,y-1])

visited = [ [ False for _ in range(N)] for _ in range(N)]

# 전체 경우의 수
cnt = 0 
# 방향
dx = [ 1, -1, 0, 0 ]
dy = [ 0, 0, 1, -1 ]

# 첫번째 지점 시작, 다음 지점 인덱스
dfs(dest[0], 1)

print(cnt)