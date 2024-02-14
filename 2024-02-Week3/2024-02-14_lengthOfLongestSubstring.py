"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans_list = []
        ans = 0
        for s_char in s:
            tmp = 0
            s_char_index = 0
            if s_char not in ans_list:
                ans_list.append(s_char)
            else:
                tmp = len(ans_list)
                s_char_index = ans_list.index(s_char)
                del ans_list[:s_char_index+1]
                ans_list.append(s_char)
            if tmp > ans:
                ans = tmp
        tmp = len(ans_list)
        if tmp > ans:
            ans = tmp
        # print(ans,ans_list)
        return  ans
    
"""
list 요소 제거할 때 index 기준, 범위로 제거할 때는 del 이용
"""