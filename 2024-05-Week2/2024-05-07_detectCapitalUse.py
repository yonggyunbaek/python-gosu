"""
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.
"""
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capital_word = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        if len(word) == 1:
            return True
        
        if word[0] in capital_word and word[1] in capital_word:
            # 1. 모두 대문자
            for w in word[1:]:
                if w not in capital_word:
                    return False
        elif word[0] in capital_word and word[1] not in capital_word:
            # 2. 첫 글자만 대문자
            for w in word[1:]:
                if w in capital_word:
                    return False
        # 3. 모두 소문자
        else:
            for w in word:
                if w in capital_word:
                    return False
            
        return True