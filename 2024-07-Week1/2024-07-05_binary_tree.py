# https://www.acmicpc.net/problem/5639

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 노드 생성
class Node:
    # 생성자: 파이썬 클래스에서 인스턴스 생성과 동시에 자동으로 호출되는 메서드
    # 생성자의 첫 번째 인자 항상 self
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, root)->None:
        self.root = Node(root) # 루트노드
    
    def search(self, value)->int:
        current_node = self.root
        while True:
            if current_node is None: # 노드가 None이면 검색 실패하고 종료
                return -1
            if current_node.value == value: # 찾음
                return current_node.value
            elif value < current_node.value: # 찾는 value가 현재 노드 value 보다 작으면 
                current_node = current_node.left # 왼쪽 서브트리에서 검색
            else: # 찾는 value가 현재 노드 value 보다 크면
                current_node = current_node.right # 오른쪽 서브트리에서 검색
    
    def insert(self, value):
        current_node = self.root
        while True:
            if value < current_node.value: # 넣으려는 value가 현재 노드 value 보다 작으면 
                if current_node.left != None:  # 이미 left 자식이 있으면
                    current_node = current_node.left  # 현재 노드를 left자식으로 바꾼다.
                else:
                    current_node.left = Node(value)  # 없다면 노드를 만들어 left자식 연결.
                    break
            else:
                if current_node.right != None:  # 이미 right 자식이 있으면
                    current_node = current_node.right  # 현재 노드를 right자식으로 바꾼다.
                else:
                    current_node.right = Node(value) # 없다면 노드를 만들어 right자식으로 연결.
                    break

    def in_order_traversal(self, node):
        if node is not None:
            self.in_order_traversal(node.left)
            print(node.value)
            self.in_order_traversal(node.right)

    # 후위순회출력
    def post_order_traversal(self, node):
        if node is not None:
            self.post_order_traversal(node.left)
            self.post_order_traversal(node.right)
            print(node.value)

# 이진 탐색 트리 생성
root = int(input())
bst = BinarySearchTree(root)

while True:
    try:
        line = input().strip()
        if line == "":
            break
        value = int(line)
        bst.insert(value)

    except EOFError:
        break

bst.post_order_traversal(bst.root)