# https://www.acmicpc.net/problem/10866

import sys
from collections import deque
input = sys.stdin.readline

class Command:
    def pushFront(self, queue, X):
        queue.appendleft(X)
        return 
    def pushBack(self, queue, X):
        queue.append(X)
        return 
    def popFront(self, queue):
        if queue:
            return queue.popleft()
        else:
            return -1
    def popBack(self, queue):
        if queue:
            return queue.pop()
        else:
            return -1
    def size(self, queue):
        return len(queue)
    def empty(self, queue):
        if len(queue) == 0:
            return 1
        else:
            return 0
    def front(self, queue):
        if len(queue) == 0:
            return -1
        else:
            return queue[0]
    def back(self, queue):
        if len(queue) == 0:
            return -1
        else:
            return queue[-1]    

n = int(input())
q = deque()
for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'push_front':
        Command().pushFront(q, cmd[1])
    elif cmd[0] == 'push_back':
        Command().pushBack(q, cmd[1])
    elif cmd[0] == 'pop_front':
        print(Command().popFront(q))
    elif cmd[0] == 'pop_back':
        print(Command().popBack(q))
    elif cmd[0] == 'size':
        print(Command().size(q))
    elif cmd[0] == 'empty':
        print(Command().empty(q))
    elif cmd[0] == 'front':
        print(Command().front(q))
    else:
        print(Command().back(q))
    