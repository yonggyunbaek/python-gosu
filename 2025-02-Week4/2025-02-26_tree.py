# https://www.acmicpc.net/problem/4803

import sys
input = sys.stdin.readline

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

class Tree:
    def __init__(self):
        self.nodes = {}
    
    def add_edge(self, nd1, nd2):
        if nd1 not in self.nodes:
            self.nodes[nd1] = TreeNode(nd1)
        if nd2 not in self.nodes:
            self.nodes[nd2] = TreeNode(nd2)

        self.nodes[nd1].children.append(self.nodes[nd2])
        self.nodes[nd2].children.append(self.nodes[nd1])

    def _dfs(self, node, visited):
        visited.add(node)
        for child in node.children:
            if child not in visited:
                self._dfs(child, visited)
    
    def countTrees(self,n):
        visited = set()
        treeCnt = 0

        for node in self.nodes.values():
            if node not in visited:
                treeCnt += 1
                self._dfs(node, visited)

        for i in range(1, n+1):
            if i not in self.nodes:
                treeCnt += 1

        return treeCnt
    
    
if __name__ == "__main__":
    cnt = 0
    while True:
        n, m = map(int, input().split())
        cnt += 1
        tree = Tree()
        if n == 0 and m == 0:
            break
        for _ in range(m):
            a,b = map(int,input().split())
            tree.add_edge(a,b)
        answer = tree.countTrees(n)
        if answer == 0:
            print(f"Case {cnt}: No trees.")
        elif answer == 1:
            print(f"Case {cnt}: There is one tree.")
        else:
            print(f"Case {cnt}: A forest of {answer} trees.")
        
