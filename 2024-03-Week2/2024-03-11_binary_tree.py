# 백준 1991
import sys
input = sys.stdin.readline

class TreeNode():
    # __init__ 메서드는 노드를 생성할 때 호출, 3개의 매개변수를 받는다. 
    # self는 현재 인스턴스를 가리킴
    def __init__(self, item, left, right):
        # 노드의 왼쪽 자식 노드
        self.left = left
        # 노드의 데이터
        self.item = item
        # 노드의 오른쪽 자식 노드
        self.right = right

# 전위순회 루트 -> 왼쪽 -> 오른쪽
def preorder(node):
    print(node.item, end = '')
    if node.left != '.':
        preorder(tree[node.left])
    if node.right != '.':
        preorder(tree[node.right])
# 중위순회 왼쪽 -> 루트 -> 오른쪽
def inorder(node):
    if node.left != '.':
        inorder(tree[node.left])
    print(node.item, end = '')
    if node.right != '.':
        inorder(tree[node.right])
# 후위순회 왼쪽 -> 오른쪽 -> 루트    
def postorder(node):
    if node.left != '.':
        postorder(tree[node.left])
    if node.right != '.':
        postorder(tree[node.right])
    print(node.item, end = '')

n = int(input())
inputs = [ list(input().split()) for _ in range(n) ]

tree = {}

for item, left, right in inputs:
    tree[item] = TreeNode(item, left, right)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])