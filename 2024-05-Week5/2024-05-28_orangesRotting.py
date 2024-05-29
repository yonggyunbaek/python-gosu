"""
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 
"""


from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh_oranges = 0
        rotten_oranges = deque()

        # 신선한 오렌지와 썩은 오렌지의 초기 위치를 파악
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    fresh_oranges += 1
                elif grid[r][c] == 2:
                    rotten_oranges.append((r, c))

        # 예외처리
        if fresh_oranges == 0:
            return 0

        ans = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        queue = rotten_oranges
        # BFS
        while queue:
            # print(queue)
            ans += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        fresh_oranges -= 1
                        queue.append((nx, ny))

        # 모든 신선한 오렌지가 썩었는지 확인
        if fresh_oranges == 0:
            return ans - 1
        else:
            return -1
