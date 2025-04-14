# https://www.acmicpc.net/problem/1389

from collections import deque, defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
relation = defaultdict(list)

# 친구 관계 저장
for _ in range(m):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)

def bfs(start):
    dist = [0] * (n + 1)
    visited = [False] * (n + 1)
    q = deque()
    # 시작점 q넣고 방문확인
    q.append(start)
    visited[start] = True

    while q:
        now = q.popleft()
        # 현재노드에서 연결된 이웃 순회
        for neighbor in relation[now]:
            # 방문 안했으면
            if not visited[neighbor]:
                # 방문확인
                visited[neighbor] = True
                # 현재노드까지거리 + 1 해서 저장
                dist[neighbor] = dist[now] + 1
                q.append(neighbor)

    return sum(dist[1:])  # 1번부터 n번까지 거리 합

min_value = float('inf')
answer = 0

# 각 사람마다 bfs 수행해서 거리 합 계산
for i in range(1, n + 1):
    total = bfs(i)
    # 최솟값 갱신
    if total < min_value:
        min_value = total
        answer = i

print(answer)

    


