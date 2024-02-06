# 다양한 입력 값으로 사물에 대해 최소 면적을 계산
# 레이더 통해 N개 점 입력값. 각각 점들은 K개의 색깔 중 하나. 색깔은 정수로 표현 {1,2,3...,K}
# 해당 색깔을 가지는 점들을 적어도 하나씩 포함하는 사물 중 넓이가 가장 작은 것을 찾아 그 넓이를 출력 - 사물은 직사각형으로 인식


def dfs(color,left,right,bottom,top):
    global minArea

    
    for point in colors[color]:
        # color 1부터
        x,y = point[0],point[1]
        # 3,7 시작
        # left 1000, right -1000, bottom 1000, top -1000
        leftN,rightN = min(left,x),max(right,x)
        bottomN, topN = min(bottom,y),max(top,y)
        area = (rightN-leftN)*(topN-bottomN)
        if minArea > area:
            if color == k:
            # color k개 확인했는지?
            # k개 확인되면 for문 반복
            # dfs 스택으로 돌면서 제일 깊은 color dfs 끝나면 for문 안돌았던 점 스택 빠져나오면서 체크하면서 minArea 갱신
                minArea = area
            else:
            # color k개 아니면 다음 컬러 점 확인
                dfs(color+1,leftN,rightN,bottomN,topN)
    return

n,k = map(int,input().split())
# n, k = 5, 3
# colors = [[], [[3,7],[5,8]], [[6,5]], [[7,1],[9,3]]]
colors =[[] for _ in range(k+1)]
for _ in range(n):
    point = list(map(int, input().split()))
    colors[point[2]].append(point[:2])
print(colors)
minArea = 2000 * 2000
dfs(1,1000,-1000,1000,-1000)
print(minArea)