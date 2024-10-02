#  https://school.programmers.co.kr/learn/courses/30/lessons/17679
def check_block(x: int, y: int, board: list) -> bool:
    if board[x][y] == " ":
        return False

    if (board[x][y] == board[x][y + 1] and
        board[x][y] == board[x + 1][y] and
        board[x][y] == board[x + 1][y + 1]):
        return True
    
    return False

def drop_block(board: list):
    row, col = len(board), len(board[0])
    
    for y in range(col):
        tmp = []
        for x in range(row):
            if board[x][y] != " ":
                tmp.append(board[x][y])
        
        # 빈 공간을 추가하여 아래로 떨어뜨리기
        for x in range(row):
            if x < row - len(tmp):
                board[x][y] = " "
            else:
                board[x][y] = tmp[x - (row - len(tmp))] if x - (row - len(tmp)) < len(tmp) else " "

def solution(m, n, board):
    board = [list(l) for l in board]
    blocks = []

    # 블록 찾기
    for x in range(m - 1):
        for y in range(n - 1):
            if check_block(x, y, board):
                blocks.append((x, y))

    # 블록 제거
    if blocks:
        for x, y in blocks:
            board[x][y] = " "
            board[x][y + 1] = " "
            board[x + 1][y] = " "
            board[x + 1][y + 1] = " "
        
        
        # 블록 떨어뜨리기
        drop_block(board)
        
        # 재귀적으로 블록 찾기
        return solution(m, n, board)
    
    return sum(y == " " for x in board for y in x)
