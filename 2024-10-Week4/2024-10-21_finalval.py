# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/submissions/

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        
        for oper in operations:
            if oper == "++X" or oper == "X++":
                X += 1
            else:
                X -= 1
        
        return X
