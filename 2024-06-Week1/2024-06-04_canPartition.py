"""
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.
"""

from collections import deque
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        
        # 총합이 홀수인 경우, 두 부분으로 나눌 수 없음
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        queue = deque([0])
        seen = set([0])
        
        for num in nums:
            for _ in range(len(queue)):
                # print("num : ", num, " queue : ", queue)
                curr_sum = queue.popleft()
                new_sum = curr_sum + num
                
                # check partition
                if new_sum == target:
                    return True
                
                if new_sum < target and new_sum not in seen:
                    queue.append(new_sum)
                    seen.add(new_sum)
                
                # 현재 합을 다시 큐에 추가하여 다음 숫자와 합산 가능하도록 함
                queue.append(curr_sum)
                seen.add(curr_sum)
        
        return False