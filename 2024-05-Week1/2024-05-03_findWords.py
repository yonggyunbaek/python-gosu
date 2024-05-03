"""
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".
"""

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row, second_row, third_row = "qwertyuiop", "asdfghjkl", "zxcvbnm"
        ans = []
        
        
        for w in words:
            status = 0
            if w[0].lower() in first_row:
                for i in range(1,len(w)):
                    if w[i].lower() not in first_row:
                        status = 1
                        break
                
            if w[0].lower() in second_row:
                for i in range(1,len(w)):
                    if w[i].lower() not in second_row:
                        status = 1
                        break
                
            if w[0].lower() in third_row:
                for i in range(1,len(w)):
                    if w[i].lower() not in third_row:
                        status = 1
                        break
            if status == 0:
                ans.append(w)
        
        return ans