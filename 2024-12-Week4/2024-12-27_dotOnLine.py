# https://www.acmicpc.net/problem/11663
# 이분탐색 함수 하나로 처리가 안됨;
import sys

input = sys.stdin.readline

def dot_min(a):  # 선분 중 가장 작은 점 인덱스 구하기 
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2

        if dots[mid] < a:
            start = mid + 1
        else:
            end = mid - 1
    return end + 1


def dot_max(b):   # 선분 중 가장 큰 점 인덱스 구하기
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2

        if b < dots[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return end

n, m = map(int,input().split())
dots = sorted(list(map(int,input().split())))

for i in range(m):
    a, b = map(int, input().split())
    print(dot_max(b) - dot_min(a) + 1)

    
