# https://www.acmicpc.net/problem/11729

import sys
input = sys.stdin.readline

# N개의 원판 start 기둥에서 end 기둥으로 옮기는데 sub를 거쳐서
def hanoi(N, start, end, sub):
    if N == 1:
        print(start, end)
    else:
        # N이 1이 아니면 N-1개의 덩어리를 start에서 sub로 
        hanoi(N-1, start, sub, end)
        # 맨밑 원판 이동
        print(start, end)
        # sub에 갔던 N-1개 덩어리 end로 이동
        hanoi(N-1, sub, end, start)

N = int(input())
print(2**N - 1)
hanoi(N, 1, 3, 2)