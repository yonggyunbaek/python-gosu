"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        
        for word in s:
            #if word.lower() in ("a","e","i","o","u"): 대소문자 모두 포함
            if word in ("a","e","i","o","u","A","E","I","O","U"):
                vowels.append(word)
                s = s.replace(word, "_", 1)
        vowels.reverse()
        #print(vowels, s)
        for v in vowels:
            s = s.replace("_", v, 1)
        return s
    
    
"""
string.replace() or list.replace()

replace('변환 대상', '값', 갯수) # 갯수 생략시 모든 대상 변환
"""