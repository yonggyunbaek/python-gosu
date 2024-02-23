"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
"""


# 실패, 브루트포스 방식
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = []
        stack = strs
        
        while stack:
            ana = [stack.pop(0)]
            stack_copy = stack.copy()

            for sc in stack_copy:
                if sorted(ana[0]) == sorted(sc):
                    ana = ana + [sc]
                    if sc in stack:
                        stack.remove(sc)
            ans.append(ana)
        return ans
    
# 풀이 / 해쉬맵 방식
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans_dict = dict()
        
        for s in strs:
            # print(sorted(s)) >> ['a', 'e', 't']
            sorted_s = ''.join(sorted(s))
            
            if sorted_s in ans_dict.keys():
                ans_dict[sorted_s] = ans_dict[sorted_s] + [s]
            else:
                ans_dict[sorted_s] = [s]

        # print(ans_dict)
        return list(ans_dict.values())

"""
브루트포스(Brute Force) 방식은 컴퓨터 알고리즘에서 매우 기본적인 해결 방법 중 하나로, 가능한 모든 경우의 수를 전부 체크하는 방식을 말합니다.
"""