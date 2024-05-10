"""
You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. 
The string is separated into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains exactly k characters, except for the first group, 
which could be shorter than k but still must contain at least one character. 
Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.

 
"""


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:

        """
        모든 그룹은 k개로 그룹핑, 맨 처음만 k보다 작을 수 있음.
        """
        result = []
        s = s.replace("-", "").upper()
        print(s)
        firstGroup = len(s) % k
        
        if firstGroup:
            result.append(s[:firstGroup])

        for i in range(firstGroup, len(s), k):
            result.append(s[i:i+k])

        return "-".join(result)
