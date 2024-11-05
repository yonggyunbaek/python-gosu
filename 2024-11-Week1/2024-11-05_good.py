# https://www.acmicpc.net/problem/1253

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

maxnum = max(nums)
nums.sort()

checklist = set()
cnt = 0
for i in range(n):
    target = nums[i]
    start = 0
    end = n - 1
    while start < end:
        # print(i, start, end, target)
        if nums[start] + nums[end] == target:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                cnt += 1
                break
        elif nums[start] + nums[end] > target:
            end -= 1
        elif nums[start] + nums[end] < target:
            start += 1


print(cnt)