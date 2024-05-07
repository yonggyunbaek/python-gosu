"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count_stones = {}
        ans = 0
        
        for s in stones:
            if s in count_stones:
                count_stones[s] += 1
            else:
                count_stones[s] = 1
        
        for j in jewels:
            if j in count_stones:
                ans += count_stones[j]
        
        return ans
    
    
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count_stones = collections.defaultdict(int)
        ans = 0
        
        for s in stones:
            count_stones[s] += 1
        
        for j in jewels:
            if j in count_stones:
                ans += count_stones[j]
        
        return ans
    
    
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count_stones = collections.Counter(stones)
        #print(count_stones)
        #Counter({'b': 4, 'A': 2, 'a': 1})
        ans = 0
        
        for j in jewels:
            if j in count_stones:
                ans += count_stones[j]
        
        return ans
    
    
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = [s in jewels for s in stones]
        #stones의 요소를 뽑아서 jewels에 있는지 비교 후 list에 추가(list comprehension)
        #print(ans)
        #[True, True, True, False, False, False, False]
        return sum(ans)

        # return sum([s in jewels for s in stones])