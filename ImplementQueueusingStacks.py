#leetcode 232

# 두 개의 stack(LIFO:Last In First Out)으로 queue(FIFO:First in First out)를 구현하시오
# 구현된 queue는 push, peek, pop, empty 기능을 지원해야함

# MyQueue class:
# void push(int x) : queue에 원소 x 입력
# int pop() : queue의 앞쪽 원소를 제거하고 제거한 원소를 반환
# int peek() : queue의 앞쪽 원소를 반환
# boolean empty() : queue가 비어 있으면 True를 반환, 반대의 경우 False를 반환

# Notes:
# 스택의 표준 기능만 사용해야함(push to top, peek/pop from top, size, is empty만 허용)
# 언어에 따라 deque(double ended queue)와 list 사용 가능

class MyQueue:

    def __init__(self):
        self.stack1 = [] # stack 정의
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x) # stack에 x값 추가

    def pop(self) -> int:
        depth = len(self.stack1) # stack 길이
        for i in range(depth-1): # stack1에 가장 처음 입력된 값만 stack1에 남김
            self.stack2.append(self.stack1.pop())
        result = self.stack1.pop() # stack1에 가장 처음 입력된 값을 제거하고 result에 그 값을 반환함
        for i in range(depth-1):
            self.stack1.append(self.stack2.pop())
        return result

    def peek(self) -> int:
        depth = len(self.stack1)
        for i in range(depth-1): # stack1에 가장 처음 입력된 값만 stack1에 남김
            self.stack2.append(self.stack1.pop())
        result = self.stack1[0] # stack1에 가장 처음 입력된 값을 result에 입력
        for i in range(depth-1):
            self.stack1.append(self.stack2.pop())
        return result
        
    def empty(self) -> bool:
        return len(self.stack1)==0
        
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
