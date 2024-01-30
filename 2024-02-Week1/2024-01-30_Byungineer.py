"""
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
"""
# list 사용
from typing import Optional
class MyStack:
    def __init__(self):
        # list 생성
        self.s_queue = []
        
    def push(self, x: int) -> None:
        # element add
        self.s_queue.append(x)

    def pop(self) -> Optional[int]:
        # element remove
        if self.s_queue:
            return self.s_queue.pop()
        else:
            return None
        #list pop, remove and return last element
        
    def top(self) -> Optional[int]:
        # get last input element
        if self.s_queue:
            return self.s_queue[-1]
        else:
            return None
    
    def empty(self) -> bool:
        # return queue status
        return not bool(self.s_queue)
        #if len(self.s_queue) == 0:
        #    return True
        #else:
        #    return False

###### Optional[int]를 사용하지 않으면, 기존의 메소드의 출력이 int 타입으로 고정되어 있기 때문에, Return되는 값으로 None을 사용할 수 없음

#deque 사용  double-ended queue의 약자로 데이터를 양방향에서 추가하고 제거할 수 있는 자료구조
from collections import deque
class MyStack:
    def __init__(self):
        self.s_deque = deque()
        
    def push(self, x: int) -> None:
        # element add
        self.s_deque.append(x)

    def pop(self) -> int:
        # element remove
        if self.s_deque:
            return self.s_deque.pop() # leftpop() 은 왼쪽에서 제거
        else:
            return None
    def top(self) -> int:
        # get last input element
        if self.s_deque:
            return self.s_deque[-1]
        else:
            return None
    def empty(self) -> bool:
        # return queue status
        return not bool(self.s_deque)
    
#queue 사용 // 자체의 top과 같은 기능은 조재하지 않음. 무조건 element 제거됨.
from queue import Queue
class MyStack:
    def __init__(self):
        self.s_queue = Queue()
        
    def push(self, x: int) -> None:
        # element add
        self.s_queue.put(x)

    def pop(self) -> int:
        # element remove
        if self.s_queue:
            return self.s_queue.get()
        else:
            return None
    def top(self) -> int:
        if not self.s_queue.empty():
            size = self.s_queue.qsize()
            for _ in range(size - 1):
                self.s_queue.put(self.s_queue.get())
            top_element = self.s_queue.get()
            self.s_queue.put(top_element)
            return top_element
        else:
            return None
    def empty(self) -> bool:
        # return queue status
        return not bool(self.s_queue)
    


"""
__init__ 함수는 MyStack 클래스(생성자)에서 자동으로 호출되는 함수(메소드). 
__init__함수는 MyStack 클래스가 인스턴스화 될 때 자동으로 호출되며, 클래스의 객체를 초기화 하는 역할을 한다.

객체(Object)는 클래스(Class)로부터 생성된 구체적인 데이터입니다. 클래스는 객체를 생성하기 위한 템플릿이라고 할 수 있습니다.
객체는 클래스의 인스턴스(Instance)라고도 불림.

객체는 클래스에서 정의한 속성과 메서드를 가지고 있으며, 이를 통해 객체의 상태와 동작을 제어할 수 있습니다. 
예를 들어, MyStack 클래스로부터 객체를 생성하여 스택을 구현한다면, 객체는 스택의 상태를 나타내는 데이터와 스택에 대한 동작을 수행하는 메서드를 가지게 됩니다.

아래는 MyStack 클래스로부터 객체를 생성하고 사용하는 간단한 예시입니다:
"""

