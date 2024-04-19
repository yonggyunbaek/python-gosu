"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

"""

# 풀이 1 / 시간초과
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        
        ans_list = [list(combi) for combi in itertools.combinations(nums,4)]
        ans = []
        for a in ans_list:
            if sum(a) == target and a not in ans:
                ans += [a]
        
        return ans

# 풀이 2 / 투포인터 
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        results = []
        n = len(nums)
        
        for i in range(n - 3):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                
                left, right = j + 1, n - 1
                
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        results.append([nums[i], nums[j], nums[left], nums[right]])
                        # 중복된 값 건너뛰기
                        while left < right and nums[left] == nums[left+1]:
                            left += 1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1
                        
                        left += 1
                        right -= 1
        return results
