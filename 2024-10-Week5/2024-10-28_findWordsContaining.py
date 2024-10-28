# https://leetcode.com/problems/find-words-containing-character/submissions/

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        answer = []
        
        for i, word in enumerate(words):
            if x in word:
                answer.append(i)
        
        return answer
