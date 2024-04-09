class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = collections.Counter(s) # 요소 갯수 파악
        seen = set() # 중복 제거
        stack = []
        
        for char in s:
            counter[char] -= 1
            
            if char in seen:
                continue
            
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
            
        return ''.join(stack)
            
        
"""
collection.Counter() 는 string or list의 요소를 key:value 형식으로 요소의 갯수를 dict로 저장하는 함수.

ex)
collection.Counter("babad")
=> Counter({'b': 2, 'a': 2, 'd': 1})
"""