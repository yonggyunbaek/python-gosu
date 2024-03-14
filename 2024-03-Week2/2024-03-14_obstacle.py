"""
https://softeer.ai/app/assessment/index.html?xid=98114&xsrfToken=uQnTokgpPEGoVGApEsKO3xEPvdjuMefJ&testType=practice
"""
import sys
from collections import deque

map_size = int(sys.stdin.readline())
map = [list(map(int,sys.stdin.readline().strip())) for _ in range(map_size)]

# print(map_size)
# print(map)

d = [[1,0],[0,1],[-1,0],[0,-1]] # move direction
visited = [[False]*(map_size) for _ in range(map_size)]

# define bfs function
def bfs(y,x):
    # 초기값
    queue = deque()
    queue.append([y,x])
    visited[y][x] = True
    count = 1

    while queue:
        tmp_y,tmp_x = queue.popleft()
        
        for i in range(4):# Up,Right,Down,Left
            cur_y = tmp_y +d[i][0]
            cur_x = tmp_x + d[i][1]

            if(0 <= cur_y < map_size and 0 <= cur_x < map_size) and map[cur_y][cur_x] ==1 and not visited[cur_y][cur_x]: 
                queue.append([cur_y,cur_x])
                visited[cur_y][cur_x] = True
                count+=1
    
    return count

results = []
for y in range(map_size):
    for x in range(map_size):
        if map[y][x] == 1 and not visited[y][x]:
            results.append(bfs(y,x))

# 블록 갯수
print(len(results))

# 블록 크기
results.sort()
for result in results:
    print(result)