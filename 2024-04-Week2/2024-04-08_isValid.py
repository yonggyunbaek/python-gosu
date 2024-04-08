class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_check = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        
        for char in s:# O(n)
            if char not in bracket_check:# dictionary Key 존재 확인 (괄호 닫힘이 아니면)
                stack.append(char)
            elif not stack or bracket_check[char] != stack.pop():
                return False
        if len(stack) == 0:
            return True
        else:
            return False
        
