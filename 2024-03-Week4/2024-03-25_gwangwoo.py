"""
문제
여름 휴가를 떠나기 위해 용돈이 필요했던 광우는 H택배 상하차 아르바이트를 지원 했다. 광우는 평소에 운동을 하지않아 힘쓰는 데에 자신이 없었지만, 머리 하나 만큼은 비상해 택배가 내려오는 레일의 순서를 조작해서 최소한의 무게만 들 수 있게 일을 하려고 한다.

레일은 N개이며, 각각의 레일은 Ni 무게 전용 레일로 주어진다. (같은 무게의 레일은 주어지지 않는다.) 레일의 순서가 정해지면 택배 바구니 무게(M)를 넘어가기 전까지 택배 바구니에 택배를 담아 들고 옮겨야 한다. 레일 순서대로 택배를 담되, 바구니 무게를 초과하지 않은 만큼 담아서 이동하게 되면 1번 일한 것으로 쳐준다. (단, 택배는 순서대로 담아야 하므로 레일의 순서를 건너 뛰어 담을 수는 없다)

총 K번 일을 하는데 최소한의 무게로 일을 할 수 있게 광우를 도와주는 프로그램을 만들어 보자.
"""


### 풀이 1 brute force, permutation
from itertools import permutations
import sys
input = sys.stdin.readline 

n, m , k = map(int,input().split())
input_rails = list(map(int,input().split()))

rails_info = permutations(input_rails, n)

result = sys.maxsize

for now_rails in rails_info:

    rails = list(now_rails)

    i = 0
    bucket = 0
    work = 0
    this_all = 0
    
    while work != k: # 작업의 수만큼만 반복
        if bucket + rails[i] <= m:  #m: 바구니 무게
            bucket += rails[i]
            rails.append(rails[i])
            i+=1
        else: 
            this_all += bucket
            bucket = 0
            work += 1
            
    result = min(result, this_all)

print(result)


### 풀이 2 / dfs 재귀함수
import sys
"""
N : 레일 갯수
M : 택배 바구니 무게
K : 일의 시행 횟수
S : 선택된 레일 조각의 수, 
V : 선택된 레일 조각의 인덱스 리스트, 
box : 선택된 레일 조각의 무게 리스트입니다.
"""
# N, M, K = sys.stdin.readline().split()
# WEIGHT_LIST = sys.stdin.readline().split()
# print(N,M,K)
# print(WEIGHT_LIST)


N, M, K = map(int, input().split())
rails = list(map(int, input().split()))
minW = 10e9


def dfs(S, V, box):
    print(f"DFS 호출 - S: {S}, V: {V}, box: {box}")  # 현재 DFS 호출 상태 출력
    if S == N:
        global minW
        nowW = basket(box)
        if nowW < minW:
            minW = nowW
        print(f"최소 무게 업데이트: {minW}")  # 최소 무게 업데이트 상황 출력
        return
    for i in range(N):
        if i not in V:
            dfs(S + 1, V + [i], box + [rails[i]])

def basket(box):
    print(f"basket 함수 호출 - box: {box}")  # basket 함수 호출 상태 출력
    tmp = 0
    idx = 0
    for _ in range(K):
        nowW = 0
        while True:
            if nowW + box[idx] > M:
                tmp += nowW
                break
            nowW += box[idx]
            idx = (idx + 1) % N
    print(f"basket 함수 결과: {tmp}")  # basket 계산 결과 출력
    return tmp

dfs(0, [], [])
print(f"최종 결과: {minW}")

### 풀이 3 / dfs while loop
import sys

N, M, K = map(int, input().split())
rails = list(map(int, input().split()))
minW = 10e9

def basket(box):
    print(f"basket 함수 호출 - box: {box}")  # basket 함수 호출 상태 출력
    tmp = 0
    idx = 0
    for _ in range(K):
        nowW = 0
        while True:
            if nowW + box[idx] > M:
                tmp += nowW
                break
            nowW += box[idx]
            idx = (idx + 1) % N
    print(f"basket 함수 결과: {tmp}")  # basket 계산 결과 출력
    return tmp

# dfs 대신 사용할 스택 초기화
stack = [(0, [], [])]  # 각 요소는 (S, V, box)를 나타냄

while stack:
    S, V, box = stack.pop()
    print(f"DFS 호출 - S: {S}, V: {V}, box: {box}")  # 현재 DFS 호출 상태 출력
    
    if S == N:
        nowW = basket(box)
        if nowW < minW:
            minW = nowW
            print(f"최소 무게 업데이트: {minW}")  # 최소 무게 업데이트 상황 출력
    else:
        for i in range(N):
            if i not in V:
                # 재귀 호출 대신 스택에 상태 추가
                stack.append((S + 1, V + [i], box + [rails[i]]))

print(f"최종 결과: {minW}")