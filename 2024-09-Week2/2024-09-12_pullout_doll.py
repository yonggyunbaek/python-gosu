# https://school.programmers.co.kr/learn/courses/30/lessons/64061
def pull_out(board, n, m):
    # 세로 검색
    for i in range(n):
        if board[i][m] != 0:
            doll = board[i][m]
            board[i][m] = 0
            return doll
        else:
            continue

def solution(board, moves):
    answer = 0
    # moves : queue
    queue = []
    n = len(board) #board size
    
    for m in moves:
        m -= 1
        doll = pull_out(board, n, m)
        if doll == None:
            # print("step0",doll)
            continue
            
        if not queue:
            queue.append(doll)
            # print("step1",doll)
            continue
            
        if queue and queue[-1] == doll:
            queue.pop()
            answer += 1
            # print("step2",doll)
        else:
            queue.append(doll)
            # print("step3",doll)
        # print(queue)
    return answer * 2
