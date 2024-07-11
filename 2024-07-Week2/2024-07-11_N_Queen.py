# https://www.acmicpc.net/problem/9663

import sys
input = sys.stdin.readline

N = int(input())
arr = [0] * N

def is_possible(r):
    for i in range(r):
        # 같은 행 확인
        if arr[r] == arr[i]:
            return False
        # 열과 열, 행과 행 차가 같으면 대각선에 존재한다는 뜻
        if r - i == abs(arr[r] - arr[i]):
            return False
    return True
    
def dfs(row):
    # 모든 row에 놓으면 종료
    if row == N:
        return 1
    
    ans = 0
    for i in range(N):
        arr[row] = i
        # row에 놓을 수 있으면 다음 row로 
        if is_possible(row):
            ans += dfs(row + 1)
    return ans

print(dfs(0))