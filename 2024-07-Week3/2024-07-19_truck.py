# https://www.acmicpc.net/problem/13335


import sys
input = sys.stdin.readline

n, w, L = map(int,input().split())
truck = list(map(int, input().split()))

bridge = [0] * w

time = 0

# 마지막 트럭이 다리 통과할때 까지
while bridge:
    # 시간 1초 경과
    time += 1
    # 다리 첫번째 요소 pop
    bridge.pop(0)
    # 다리 안 건넌 트럭 있으면
    if truck: 
        # 다리 무게 제한 안걸리면 다리에 append
        if sum(bridge) + truck[0] <= L:
            bridge.append(truck.pop(0))
        else:
            # 트럭이 남아있는데 무게 때문에 못올리면 0으로 자리 채우기
            bridge.append(0)

print(time)
