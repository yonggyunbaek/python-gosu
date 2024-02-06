"""
Write a function that reverses a string. The input string is given as an array of characters s.

You must do this by modifying the input array in-place with O(1) extra memory.
"""

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()
        
        
"""
s를 반환하지 않고 자체를 수정해야 하기 때문에, s = s[::-1] 과 같은 방법을 사용할 수 없음.

번외로 파이썬에서는 List가 Mutable(가변) 속성임.

리스트를 얕은 복사를 하면, 복사된 리스트 수정시 원본도 수정이 된다는 뜻

다음은 그 예시

a_list = [1, 2, 3]
b_list = a_list  # 리스트 복사

a_list.append(4)  # a_list를 수정

print(a_list)  # 출력: [1, 2, 3, 4]
print(b_list)  # 출력: [1, 2, 3, 4]

"""