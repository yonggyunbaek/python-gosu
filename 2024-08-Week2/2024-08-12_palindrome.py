# https://www.acmicpc.net/problem/1213

import sys
# from itertools import permutations
input = sys.stdin.readline

### 전체 경우의수 만들어서 palindrome인지 확인하는 건 시간이 오래걸림

# def is_palindrome(word):
#     for left in range(len(word) // 2):
#         right = len(word) - left -1
#         if word[left] != word[right]:
#             return 
#     return word

# name = input().rstrip()

# for perm in permutations(name):
#     word = ''.join(perm)
#     print(word)
#     if is_palindrome(word):
#         print(word)
#         break
# else:
#     print("I'm Sorry Hansoo")


### Counter 딕셔너리 만들고 홀수개인 문자 체크
### 홀수개인 문자 1개면 palindrome으로 만들기
from collections import Counter

def make_palindrome(word):
    count_dict = Counter(word)
    odd_char = ''
    half = []

    for char, count in sorted(count_dict.items()):
        # 홀수개인 문자는 하나만 가능
        # 문자개수가 홀수이면
        if count % 2 == 1:
            # 홀수개수 문자가 이미 있으면 리턴
            if odd_char:
                return "I'm Sorry Hansoo"
            # 홀수개수 문자가 없으면 지정
            odd_char = char
        # 문자개수가 짝수면 
        # half 리스트에 절반만 append
        half.append(char * (count // 2))
    
    left_half = ''.join(half)
    right_half = ''.join(reversed(half))
    return left_half + odd_char + right_half

name = input().rstrip()
answer = make_palindrome(name)
print(answer)