from collections import deque
import sys

input = sys.stdin.readline

def get_next_numbers(n):
    return [n + 1, n - 1, n * 2]

def bfs():
    cnt = 0
    while q:
        size = len(q)
        for _ in range(size):
            now = q.popleft()
            if now == k:
                return cnt
            else:
                for next in get_next_numbers(now):
                    if next < 0 or next >= 100001:
                        continue
                    if visited[next] == 0:
                        q.append(next)
                        visited[next] = 1
        cnt += 1
        print(q, cnt)
    return cnt


n, k = map(int, input().split())
q = deque()
visited = [0] * 100001
q.append(n)
visited[n] = 1

print(bfs())