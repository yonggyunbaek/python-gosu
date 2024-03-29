# 선아는 미생물 연구중, 미생물 여러 마리를 한 줄로 나열하면 한 마리만 남을 때까지 규칙에 따라 미생물들이 서로 흡수한다
# 1. 하루 한 번 줄의 맨 앞에 미생물 부터 차례대로 인접한 미생물 중 자신보다 크기가 작거나 같은 것들을 전부 흡수, 흡수하면 크기는 합만큼
# 2. 만약 3,2,1 이면 하루 뒤 5, 1
# 3. 흡수하는 미생물은 하루에 흡수할 모든 미생물을 한 번에 흡수 3,4,5 면 4의 차례에서 7,5가 된다. 7이 된 후 같은 날 5를 흡수 못한다.

# N 마리 일 때 마지막 남는 미생물 최종 크기와 초기 위치를 찾는 프로그램

import sys

def find_last_micro(visited, idx_micro):
    # print("len", len(idx_micro))
    
    if len(idx_micro) == 1:
        return idx_micro
    
    for i in range(len(idx_micro)):
        print(idx_micro)
        print(visited)
        print("i=", i)
        if len(idx_micro) == 1:
            # return idx_micro
            break
        
        elif visited[i] == False:
            if i-1 >= 0 and idx_micro[i][1] >= idx_micro[i-1][1]:
                idx_micro[i][1] += idx_micro[i-1][1]
                idx_micro.pop(i-1)
                visited.pop(i-1)
                print("이전 흡수")
                visited[i-1] = True
                find_last_micro(visited, idx_micro)

            elif i < len(idx_micro) and idx_micro[i][1] >= idx_micro[i+1][1]:
                idx_micro[i][1] += idx_micro[i+1][1]
                idx_micro.pop(i+1)
                visited.pop(i+1)
                print("다음 흡수")
                visited[i] = True
                find_last_micro(visited, idx_micro)

            else:
                print("pass")
                visited[i] = True
                pass
        elif visited == [ True ] * len(idx_micro):
            visited = [ False ] * len(idx_micro)
            

        else:
            pass


N = int(input())
micro = list(map(int, sys.stdin.readline().split()))
index = [i+1 for i in range(N)]

idx_micro = [ [i+1, micro[i]] for i in range(N)]
# print(idx_micro)
visited = [ False ] * len(idx_micro)
find_last_micro(visited, idx_micro)
print(idx_micro[0][1])
print(idx_micro[0][0])