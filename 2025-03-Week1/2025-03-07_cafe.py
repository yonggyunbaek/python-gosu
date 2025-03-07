# https://www.acmicpc.net/problem/1275

from math import ceil, log
import sys
input = sys.stdin.readline

def segment(left, right, i=1):
    # i는 구하려는 인덱스, left는 구간 범위 왼쪽, right는 구간 범위 오른쪽
    if left == right:
        # 구간 길이가 1이면 리프노드니까, 트리에 자기 자신을 저장
        tree[i] = nums[left]
        return tree[i]
    # 범위에 노드가 두개 이상이면 범위를 절반으로 나누고
    mid = (left + right) // 2
    # segment에 대한 연산을 노드에 저장
    tree[i] = segment(left, mid, i*2) + segment(mid+1, right, i*2+1)
    return tree[i]

# 구간 합 구하기
def search(start, end, left, right, i=1):
    # start = 구간 범위 왼쪽, end = 구간 범위 오른쪽
    # left = 찾는 범위 왼쪽, right = 찾는 범위 오른쪽
    # 찾는 범위가 구간을 벗어나면 0을 리턴
    if end < left or start > right:
        return 0

    # 찾는 범위 왼쪽이 구간 왼쪽보다 작거나 같고,
    # 찾는 범위 오른쪽이 구간 오른쪽보다 크거나 같으면 구간값 리턴
    if left <= start and end <= right:
        return tree[i]

    # 모두 아니라면 구간을 절반으로 나누고,
    mid = (start + end) // 2
    return search(start, mid, left, right, i*2) + search(mid+1, end, left, right, i*2+1)

def update(start, end, idx, diff, i=1):
    if start > idx or idx > end:
        return
    tree[i] += diff
    if start != end:
        mid = (start + end) // 2
        update(start, mid, idx, diff, i*2)
        update(mid+1, end, idx, diff, i*2+1)

n, q = map(int,input().split())
nums = list(map(int,input().split()))
tree = [0] * 2**(ceil(log(n, 2) + 1))
segment(0,n-1)
# print(tree)
# [0, 15, 6, 9, 3, 3, 4, 5, 1, 2, 0, 0, 0, 0, 0, 0]
for _ in range(q):
    x,y,a,b = map(int,input().split())
    if x > y:
        x, y = y, x
    print(search(0,n-1,x-1,y-1))
    diff = b - nums[a-1]
    nums[a-1] = b  
    update(0, n-1, a-1, diff)