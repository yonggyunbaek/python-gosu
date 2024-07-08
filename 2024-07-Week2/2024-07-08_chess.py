import sys
input = sys.stdin.readline

n,m = map(int,input().split())

board = []
cnt = []
for _ in range(n):
    board.append(input().strip())

# i,j 체스판 시작점
for i in range(n-7):
    for j in range(m-7):
        # W로 시작할 경우 개수
        w_idx = 0
        # B로 시작할 경우 개수
        b_idx = 0
        # i,j 부터 시작해서 8X8 탐색
        for x in range(i,i+8):
            for y in range(j,j+8):
                # 각 자리 인덱스 합이 짝수면
                if (x+y) % 2 == 0:
                    # 시작이 W고 현재 탐색 값이 B이면
                    if board[x][y] != 'W':
                        # W로 칠하는 개수
                        w_idx += 1
                    # 시작이 B고 현재 W이면
                    else:
                        # B로 칠하는 개수
                        b_idx += 1

                # 각 자리 인덱스 합이 홀수면
                else:
                    # 시작이 W고 현재 탐색 값이 B이면
                    if board[x][y] != 'W':
                        # B로 칠하는 개수
                        b_idx += 1
                    # 현재 W이면
                    else:
                        # W로 칠하는 개수
                        w_idx += 1                    

        cnt.append(w_idx) #W로 시작할 때 경우의 수
        cnt.append(b_idx) #B로 시작할 때 경우의 수
print(min(cnt))