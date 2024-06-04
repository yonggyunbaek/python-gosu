"""
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.
"""


from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        collections.Counter > 요소 갯수를 dict형태로.
        Counter().most_common(x) x갯수 만큼 상위 key 반환
        """
        rank_nums = list(map(list, Counter(nums).most_common(k)))
        # print(rank_nums)
        
        ans = []
        for r in rank_nums:
            ans.append(r[0])
            
        return ans
    
    
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_freq = defaultdict(int)
        for n in nums:
            nums_freq[n] += 1

        # 빈도수 기준 정렬
        sorted_items = sorted(nums_freq.items(), key=lambda x: x[1], reverse=True)

        ans = [item[0] for item in sorted_items[:k]]
        return ans
