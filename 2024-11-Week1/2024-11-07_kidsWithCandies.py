# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/submissions/

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        answer = []
        m = max(candies)
        
        for candy in candies:
            if candy + extraCandies < m:
                answer.append(False)
            else:
                answer.append(True)
                
        return answer
