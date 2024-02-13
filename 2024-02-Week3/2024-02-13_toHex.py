"""
Given an integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.

All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve this problem.
-2^31 <= num <= 2^31 - 1 
"""
# 틀린 풀이 : 음수 표현 불가능
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            hex_n = "0"
        elif num < 0:
            hex_n = "ffffffff"
        else:
            hex_n = hex(num)[2:]
        return hex_n
    
    
# 풀이 1
# bitshift
class Solution:
    def toHex(self, num: int) -> str:
        ans = self.bitshift(num,5)
        return ans[2:]
    def bitshift(self, n:int, nbit: int) -> int:
        hex_n = (n + (1 << 2**nbit)) % (1 << 2**nbit)
        return hex(hex_n)

# 풀이2
# Bit masking
class Solution:
    def toHex(self, num: int) -> str:
        ans = self.bitshift(num,32)
        return ans[2:]
    def bitshift(self, n:int, nbit: int) -> int:
        hex_n = (n & (2**nbit - 1))
        return hex(hex_n)

"""
hex() 함수를 이용하면, 10진수를 16진수 문자열로 반환할 수 있다.
하지만, 음의 정수가 element로 들어가면,
hex(-1) -> '-0x1' 과 같이 부호가 붙으며 정수부분이 그대로 변환되어 반환된다.
C, C++과 같이 자료형의 크기를 명시하는 언어의 경우에는 다음과 같이 출력되어야 한다.
1byte(8bit) -1 -> 0xFF   -128 -> 0x80
4byte(32bit) -1 -> 0xFFFFFFFF     -128 -> 0xFFFFFF80

위 표현식은 2의 보수(two's complement)와 관련있음.


@@@ 2의 보수
컴퓨터(CPU)를 구성하는 가장 중요한 요소는 레지스터와 ALU인데, 정수형 처리는 ALU에서 이루어진다. 레지스터도 그렇고 ALU도 그렇고 설계 상 비트수를 결정하고 만들어야 한다. CPU의 비트수 제한으로 인해 이진법 계산의 적용에서 비트를 벗어나면 버리게 된다.



문제의 조건 -2^31 <= num <= 2^31 - 1 >> num은 32bit, 4byte 크기형으로 제한해야 한다.


# 비트 연산자(Bitwise Operators)
# 2의 누승 출력하기
a = 1
for i in range(0, 11):
    print('{0:6,}'.format(a << i), end=' ')
print()

a = 2
for i in range(0, 11):
    print('{0:6,}'.format(a ** i), end=' ')
print()
"""

