"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rN_list = []
        mag_list = []
        for r in ransomNote:
            rN_list.append(r)
        for m in magazine:
            mag_list.append(m)
        
        while len(rN_list) >= 1:
            try:
                tmp = rN_list.pop()
                mag_list.remove(tmp)
            except:
                return False
        return True