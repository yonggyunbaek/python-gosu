"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
"""

#풀이1. while loop
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans_list = []
        stack = [(0, 0, '')] 
        
        while stack:
            left_bracket, right_bracket, ans = stack.pop()
            
            if len(ans) == n * 2:
                ans_list.append(ans)
            
            if right_bracket < left_bracket:
                stack.append((left_bracket, right_bracket + 1, ans + ')'))
            
            if left_bracket < n:
                stack.append((left_bracket + 1, right_bracket, ans + '('))
        
        return ans_list
    
    
#풀이2. 재귀함수

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans_list = []    
        self.dfs(0, 0, '', n, ans_list)
        return ans_list
    
    def dfs(self, left_bracket, right_bracket, ans, n, ans_list):
        if len(ans) == n * 2:
            ans_list.append(ans)
            return
        
        if left_bracket < n:
            self.dfs(left_bracket + 1, right_bracket, ans + '(', n, ans_list)
        
        if right_bracket < left_bracket:
            self.dfs(left_bracket, right_bracket + 1, ans + ')', n, ans_list)