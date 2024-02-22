"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        stack = [[[], 0, 0]] # 조합, 합계, index : for문 반복시 중복 방지
        ans_list = []
        
        while stack: #stack에 값이 있을 때 까지.
            candidate_list, candidate_sum, index = stack.pop(0)
            
            # target과 일치 시 리스트 정답 배열에 추가
            if candidate_sum == target:
                ans_list.append(candidate_list)
            
            # target 추적을 위한 반복 더하기
            if candidate_sum < target:
                for i in range(index,len(candidates)): #[2,3,6,7]에서 3에서 조합을 찾으면, 2를 사용하면 안됨(중복 발생)
                    current_candidate_list = candidate_list + [candidates[i]]
                    current_candidate_sum = candidate_sum + candidates[i]
                    stack.append([current_candidate_list, current_candidate_sum, i])
        
        return ans_list