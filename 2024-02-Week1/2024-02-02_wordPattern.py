"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        ans_dict = {}
        s_list = s.split()
        
        if len(s_list) == len(pattern):
            for p, s_ele in zip(pattern, s_list):
                if s_ele not in ans_dict.values() and ans_dict.get(p) == None:                
                    ans_dict[p] = s_ele
                elif p in ans_dict and ans_dict[p] == s_ele:
                    continue
                else:
                    return False
            return True
        else:
            return False
        
        
"""
if ans_dict[p] == s_ele:
만약 dictionary에 키가 없는데 위와 같은 조건을 쓰면 에러가 발생한다...

Dictionary 사용법 정리
0. 선언
a_dict = {}
a_dict = dict()

1. key:value 추가, 갱신
a_dict[key] = value

2. value 반환
a_dict[key]

3. key:value 삭제
del a_dict[key]

4. values, keys, items
a_dict.keys() : key 목록을 list로 반환
a_dict.values() : values 목록을 list 반환
a_dict.items() : Key:value 쌍을 list로 반환

5. get 이용
key 존재하지 않는데 접근 시 에레 발생, Key 존재 여부 확인시에 사용
a_dict.get(key) == None >> 키 없으면 True 반환

6. 참고
key in a_dict >> dict에 key 존재시 True, 없으면 False
"""