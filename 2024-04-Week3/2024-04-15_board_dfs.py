class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        
        def dfs(x, y, index):
            # word의 모든 글자를 찾은 경우
            if index == len(word):
                return True
            # 범위를 벗어나거나, 이미 방문했거나, 현재 글자가 word[index]와 일치하지 않는 경우
            if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or board[x][y] != word[index]:
                return False
            
            # 현재 위치 방문 처리
            visited[x][y] = True
            
            # 상하좌우 탐색
            found = dfs(x+1, y, index+1) or dfs(x-1, y, index+1) \
                    or dfs(x, y+1, index+1) or dfs(x, y-1, index+1)
            
            # 탐색 후에는 방문 처리를 원래대로 되돌림
            visited[x][y] = False
            
            return found
        
        for i in range(m):
            for j in range(n):
                # 주어진 단어의 첫 글자와 일치하는 board의 모든 위치에서 DFS 시작
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        
        return False
