"""
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        s_dict = {}
        for char in s:
            if s_dict.get(char) == None:
                s_dict[char]=1
            else:
                s_dict[char]="2+"
        
        for k, v in s_dict.items():
            if v == 1:
                return s.find(k)
            else:
                continue
        return -1
                
            
            
