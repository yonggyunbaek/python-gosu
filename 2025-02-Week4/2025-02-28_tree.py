# https://www.acmicpc.net/problem/1068

import sys
input = sys.stdin.readline

def dfs(v):
    # 인덱스 = 노드 번호, tree는 인덱스에 연결된 부모노드
    # v번째 노드를 지운다 -> v번 노드의 부모노드는 더이상 없다
    tree[v] = -2
    # 전체 노드 순회
    for i in range(n):
        # 노드(i)의 부모노드 tree[i]와 지울 노드번호가 같다면  = i의 부모노드가 지울 노드번호와 같다면
        if v == tree[i]:
            # 노드 i도 지운다 = child노드 지우기
            dfs(i)

n = int(input())
tree = list(map(int,input().split()))
remove = int(input())

dfs(remove)
cnt = 0

for i in range(n):
    # tree는 부모노드 리스트니까 -2는 부모노드가 없음을 뜻하므로 제외
    # 인덱스번호(노드)가 부모노드 리스트에 없다면 리프노드를 의미
    if tree[i] != -2 and i not in tree:
        cnt += 1

print(cnt)