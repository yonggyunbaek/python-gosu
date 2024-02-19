"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
"""

#풀이
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters={
            2:["a","b","c"],
            3:["d","e","f"],
            4:["g","h","i"],
            5:["j","k","l"],
            6:["m","n","o"],
            7:["p","q","r","s"],
            8:["t","u","v"],
            9:["w","x","y","z"]
        }
        if len(digits)==0:
            return []

        ans = []
        ans_tmp = [[]]

        for n in digits:
            #initialize
            ans = ans_tmp
            ans_tmp = []
            print(ans_tmp)

            for a in ans: # [['a'],['b'],['c']]
                for l in letters[int(n)]:
                    ans_tmp.append(a + [l]) # list element 연산 ['a'] + ['e'] = ['a','e']
         
        # 리스트 내의 리스트를 문자열로 변환하여 반환
        return [''.join(tmp) for tmp in ans_tmp]