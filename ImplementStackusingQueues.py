#leetcode 225

# 두 개의 queue(FIFO:First In First Out)로 stack(LIFO:Last In First Out)을 구현하시오
# 만들어진 스택은 push, top, pop, empty 기능을 지원해야함

# void push(int x) : x를 스택의 맨 위에 데이터를 넣습니다
# int pop() : 스택 가장 위의 데이터를 제거하고 return 합니다
# int top() : 스택 가장 위의 데이터를 return 합니다
# boolean empty() : 스택이 비었다면 true 반대의 경우 false를 반환합니다

# Notes
# 큐의 표준 기능만 사용해야함(push to back, peek/pop from front, size, is empty 기능만 유효함)
# 언어에 따라 queue가 적용되지 않을 수 있으므로, list와 deque 를 사용할 수 있습니다

from collections import deque

class MyStack:

    def __init__(self):
        self.queue1 = deque() # deque 정의
        self.queue2 = deque()
        self._top = None

    def push(self, x: int) -> None:
        self.queue1.append(x) # append(x) : deque의 맨 끝(오른쪽)에 x를 추가, 시간복잡도 : O(1)
        self._top = x

    def pop(self) -> int: # 시간복잡도 : O(n)
        while len(self.queue1)>1: # queue1의 길이가 1보다 클 때,
            self._top = self.queue1.popleft() # queue1의 맨 앞 원소를 1개 삭제 후 _top으로 반환(가장 나중에 입력된 원소)
            self.queue2.append(self._top) # queue2의 맨 끝에 반환 값을 추가
        result = self.queue1.popleft() # queue1의 맨 앞 원소를 1개 삭제 후 result으로 반환(가장 나중에 입력된 원소)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return result

    def top(self) -> int:
        return self._top

    def empty(self) -> bool:
        return len(self.queue1)==0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
