# https://www.acmicpc.net/problem/1517
# 버블정렬로 풀면 시간초과
# 병합정렬
import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))


# def bubble_sort(array):
#     cnt=0
#     for i in range(len(array)):
#         for j in range(len(array)-i-1):
#             if (array[j] > array[j+1]):
#                 temp = array[j]
#                 array[j] =array[j+1]
#                 array[j+1] = temp
#                 cnt+=1
#     return(cnt)
# print(bubble_sort(A))

# left와 right를 가지고 새로운 리스트 만들기
def merge(start, end):
    global cnt
    mid = (start + end) // 2
    i, j = start, mid + 1
    new_arr = []

    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            new_arr.append(arr[i])
            i += 1
        else:
            new_arr.append(arr[j])
            j += 1
            cnt += mid +1 -i
    
    if i <= mid:
        new_arr += arr[i:mid+1]
    if j <= end:
        new_arr += arr[j:end+1]
    
    for i in range(len(new_arr)):
        arr[start + i] = new_arr[i]

# 모든 원소를 나누기 위한 단계 
# 재귀적으로 반씩 나누고 앞(left)쪽 반 나누고 안나눠지면 merge수행 
# 재귀적으로 쪼개면서 start, mid 구하고 mid+1이 end랑 같아지면 merge해서 정렬하고 cnt 누적
def merge_sort(start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(start, mid)
        merge_sort(mid + 1, end)
        # merge에서 cnt 찾음
        merge(start, end)

# cnt는 역순 쌍의 개수
cnt = 0
merge_sort(0, N-1)
print(cnt)