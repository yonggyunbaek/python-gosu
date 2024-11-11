# https://www.acmicpc.net/problem/1939

import sys
from collections import deque
input = sys.stdin.readline

def bfs(midWeight):
    queue = deque()
    # 큐에 시작 지점(노드) x 넣는다
    queue.append(one)
    visited = [False] * (n+1)
    visited[one] = True

    # 큐가 빌 때 까지 반복
    while queue:
        # 큐에서 노드를 빼고
        x = queue.popleft()
        # 연결된 노드(i) 만큼 반복
        for i, w in bridges[x]:
            # 아직 방문 안했고 중량 제한(w)가 현재 체크하는 값(midWeight) 보다 크면
            if not visited[i] and w >= midWeight:
                # 방문처리하고 큐에 추가
                visited[i] = True
                queue.append(i)
    # 큐가 비었을 때(연결된 노드 확인 끝났을 때) visited[two] 에 방문을 했으면 == 목적지에 도달 했으면
    if visited[two]: 
        return True
    else:
        return False


n, m = map(int, input().split())
bridges = [ [] for _ in range(n+1) ]

for i in range(m):
    a,b,c = map(int, input().split())
    bridges[a].append([b,c])
    bridges[b].append([a,c])

# print(bridges)
# [[], [[2, 2], [3, 3]], [[1, 2], [3, 2]], [[1, 3], [2, 2]]]

one, two = map(int, input().split())

# 중량 start, end
start, end = 1, 1000000000

# 찾는 값 mid로 갱신
result = 0

while start <= end:
    mid = (start + end) // 2
    # bfs(mid) 가 true이면 x -> y 까지 도달 가능하므로 result 갱신하고 중량 늘려서 테스트
    if bfs(mid):
        result = mid
        start = mid + 1
    # bfs(mid) 가 false이면  x -> y 까지 도달 안되므로 중량 줄여야함
    else:
        end = mid - 1

print(result)