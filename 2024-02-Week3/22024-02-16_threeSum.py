"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""

# 풀이1 / 실패
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        left = 0
        right = len(nums) - 1

        nums.sort()
        # print(nums)
        while left < right:
            #1. nums[left] + nums[right] > 0 / mid right에서 -= 1 & left += 1
            if nums[left] + nums[right] >= 0:
                for mid in range(left+1, right):
                    print("@@@@", left, mid, right)
                    if nums[left] + nums[mid] + nums[right] == 0:
                        ans.append((nums[left],nums[mid],nums[right]))
                right -= 1
                continue
                    
            #2. nums[left] + nums[right] < 0 / mid left에서 += 1 & right -= 1
            if nums[left] + nums[right] < 0:
                for mid in range(right-1, left, -1):
                    print(left, mid, right)
                    if nums[left] + nums[mid] + nums[right] == 0:
                        ans.append((nums[left],nums[mid],nums[right]))
                left += 1
                continue
        ans = list(set(ans))
        return ans


# 풀이2 / 패스
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:  # 중복된 값 건너뛰기
                continue
            left, right = i+1, len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    result.append((nums[i], nums[left], nums[right]))
                    while left < right and nums[left] == nums[left + 1]:  # 중복된 값 건너뛰기
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:  # 중복된 값 건너뛰기
                        right -= 1
                    left += 1
                    right -= 1

        return result
