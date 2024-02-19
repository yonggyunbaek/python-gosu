# 백준 20055
# 길이 N 컨베이어 벨트
# 2N 짜리 벨트가 위아래로 감싸며 돈다. 1간격으로 2N개의 칸, 칸마다 1~2N 번호
# i번 칸의 내구도 Ai
# 2N 에서 올라가면 1 (올리는 위치) / N(내리는 위치)에서 내려가면 N+1 
# 로봇은 올리는 위치에만 올린다 내리는 위치에 도달하면 내린다


import sys
input = sys.stdin.readline

# 로봇 + 벨트 회전
def rotate_with_robot():
    l_belt = belt[-1]
    belt[1:] = belt[0:2*N - 1]
    belt[0] = l_belt

    robots[1:] = robots[0:N-1]
    robots[0] = 0

# 로봇이 스스로 이동
def move_robot():
    # 가장먼저 올라간 로봇이 이동해야 하므로 뒤에서부터 체크
    for i in range(N-1,-1,-1): # N-1 부터 0까지 역순으로
        if robots[i]: # 로봇이 있으면
            if i == N-1: #로봇이 내리는 위치면 내려
                robots[i] = 0
            else:
                # 내리는 위치 아니면 로봇이 없고, 내구도가 0보다 크면 이동
                # 이동후 내구도 -1
                if not robots[i+1] and belt[i+1]:
                    robots[i] = 0
                    robots[i+1] = 1
                    belt[i+1] -= 1
# 로봇 올리기
def raise_robot():
    if belt[0]:
        robots[0] = 1
        belt[0] -= 1

N, K = map(int, input().split())
belt = list(map(int,input().split()))
robots = [0]*N
cnt = 0

while belt.count(0) < K:
    cnt += 1
    rotate_with_robot()
    move_robot()
    raise_robot()
    print(belt)
    
print(cnt)