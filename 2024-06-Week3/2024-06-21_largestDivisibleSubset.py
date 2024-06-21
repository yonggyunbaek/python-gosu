"""
Given a set of distinct positive integers nums, return the largest subset answer such that every pair (answer[i], answer[j]) of elements in this subset satisfies:

answer[i] % answer[j] == 0, or
answer[j] % answer[i] == 0
If there are multiple solutions, return any of them.
"""
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()
        n = len(nums)
        dp = [1] * n
        prev = [-1] * n

        max_len = 1
        max_idx = 0

        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev[i] = j

            if dp[i] > max_len:
                max_len = dp[i]
                max_idx = i

        # 최대 부분집합 구성
        result = []
        while max_idx != -1:
            result.append(nums[max_idx])
            max_idx = prev[max_idx]

        return result[::-1]

"""
1. Sort the Array ( ascending order )
2. For Each Element traverse the previous element
3. If element is divisible by any previous element it means it can be part of that group by we also need to make sure it is part of the group with maximum size, So if we found any bigger group we will add it to that group
4. If we update the group size, it means we have added new element I will update my previous of the current element with group's maximum till now ( before adding )
5. I will also track the index of the last element added in the biggest group
6. Now I will backtraverse from that maximum index ( defined in previous point ) using my previous element array and one by one add into my result list
"""