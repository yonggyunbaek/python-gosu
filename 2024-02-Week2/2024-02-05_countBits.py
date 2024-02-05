"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

0~n까지의 수를 2진법으로 변환, 1의 갯수를 리스트에 추가 및 반환

"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans_list = []
        for num in range(0,n+1):
            ans = bin(num).count("1")
            ans_list.append(ans)
            
        return ans_list
    
    
"""
count : 문자열 내에 특정 문자의 갯수 반환.
bin : 10진수를 binary 반환, string 타입이며 0b이 헤드에 붙음. 2진수라는 의미

"""