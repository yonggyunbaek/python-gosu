# https://www.acmicpc.net/problem/17299

import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums_count = Counter(nums)
result = [-1] * n
stack = [0]
# print(stack, result, nums, nums_count)
for i in range(1, n):
    # print(stack, result)
    # 현재 숫자가 스택 가장 위에 값을 인덱스로 nums[stack[-1]] 의 빈도수 보다 크면
    while stack and nums_count[nums[stack[-1]]] < nums_count[nums[i]]:
            # stack에서 pop한 숫자를 인덱스로 결과 리스트에 현재 숫자 할당
            result[stack.pop()] = nums[i]
    stack.append(i)
    # print(stack, result)
print(*result)

    
    

