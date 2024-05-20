"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        
        def dfs(i,j):
            
            if i < 0 or i >= len(grid) or \
                j< 0 or j >= len(grid[0]) or \
                grid[i][j] != '1':
                    return # None return 하며 함수 종료
            
            # else:
            # 재탐색 방지 
            grid[i][j] = 0
            
            # 상하좌우 탐색
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)


        for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == '1':
                        # 육지 탐색 / 재귀로 모두 찾으며, 이미 탐색한 부분은 0으로 바꿈
                        dfs(i,j)
                        ans += 1
        
        return ans