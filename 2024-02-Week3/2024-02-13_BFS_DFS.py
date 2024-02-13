# 백준 1260

import sys
input = sys.stdin.readline

def dfs(node):
    global visited
    # 방문 확인
    visited[node] = True
    print(node, end = ' ')
    for next in range(1, N+1): # 1부터 N까지 확인
        # 방문안했고 그래프 연결 되어 있으면 dfs 호출
        if not visited[next] and graph[node][next]:
            dfs(next)
            # 호출 될때마다 방문 확인되고 출력

def bfs():
    global q, visited
    # q요소 있으면 계속 반복
    while q: 
        cur = q.pop(0) # 시작 노드
        print(cur, end = ' ')
        # cur 에서 갈 수 있는 곳 확인해서 q에 추가
        for next in range(1, N + 1):
            if not visited[next] and graph[cur][next]:
                visited[next] = True
                q.append(next)


#노드수, 간선, 시작노드
N, M, V = map(int, input().split())

# (N+1) x (N+1) 크기의 그래프 생성
# N+1 로 index 헷갈리지 않게 
graph = [[False] * (N + 1) for i in range(N + 1)]
# 방문 리스트
visited = [False] * (N + 1)

# graph 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True


dfs(V)
print()

# bfs 출력하기 위해 visited 초기화
visited = [False] * (N + 1)
q = [V]
visited[V] = True
bfs()