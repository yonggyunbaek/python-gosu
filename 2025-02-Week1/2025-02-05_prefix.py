# https://www.acmicpc.net/problem/14426

import sys
input = sys.stdin.readline

# 시간초과
# n,m = map(int,input().split())
# s = [ input().rstrip() for _ in range(n) ]
# cnt = 0
# for _ in range(m):
#     p = input().rstrip()
#     l = len(p)
#     for i in s:
#         if i[:l] == p:
#             cnt += 1
#             break
# print(cnt)

# 노드 구현
class Node(object):
    # key 값으로 입력될 문자
    # data 문자열 종료 flag
    # children 자식노드 저장
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


# Trie 구현
class Trie:
    def __init__(self):
        # head 빈 노드 생성
        self.head = Node(None)

    # 트리 생성
    def insert(self, string):
        current_node = self.head

        for char in string:
            # 문자열의 문자를 하나씩 children에 있는지 확인 후 없으면 저장하고 
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            # 현재 노드 갱신
            current_node = current_node.children[char]
        # 문자열을 다 돌면 data에 문자열 저장(flag)
        current_node.data = string
    
    # 문자열 존재하는지 여부 리턴
    def search(self, string):
        current_node = self.head
        
        for char in string:
            # 문자열의 문자를 하나씩 children에 있는지 확인하여 있으면 다음 노드로 넘어가기(이어서 확인)
            if char in current_node.children:
                current_node = current_node[char]
            else:
                return False
        # 마지막 노드에 data(flag)가 있으면 문자열이 존재하니까 True
        if current_node.data:
            return True
        else:
            return False

    # prefix로 시작하는 단어 있는지
    def startWith(self, prefix):
        current_node = self.head
        
        # prefix를 따라 내려가면서 마지막 노드에 도달
        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return False
        
        return True  # 만약 prefix가 트리 안에 존재한다면 True 리턴

n,m = map(int,input().split())
wordList = [ input().rstrip() for _ in range(n) ]
cnt = 0
trie = Trie()
for word in wordList:
    trie.insert(word)

for _ in range(m):
    prefix = input().rstrip()
    if trie.startWith(prefix):
        cnt += 1
print(cnt)