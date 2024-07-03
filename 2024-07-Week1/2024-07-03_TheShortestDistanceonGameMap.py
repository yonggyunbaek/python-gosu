"""
https://school.programmers.co.kr/learn/courses/30/lessons/1844
"""

from collections import deque
def solution(maps):
    n, m = len(maps), len(maps[0])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    def bfs(x, y):
        queue = deque([(x, y)])
        maps[x][y] = 1
        while queue:
            x, y = queue.popleft()
            if x == n - 1 and y == m - 1:
                return maps[x][y]
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    queue.append((nx, ny))
        return -1

    return bfs(0, 0)
