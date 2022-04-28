# leetcode 1823

# n명의 사람들이 1~n까지의 번호가 시계방향으로 배정된 원탁에 앉아 게임을 하고 있습니다.
# * i번째 사람은 i+1번째 사람 옆에 앉아 있으며 n번째 사람은 첫번째 사람 옆에 앉아 있습니다.

# 게임의 룰은 다음과 같습니다.
# 1. 첫번째 사람이 시작합니다.
# 2. 시작한 사람부터 시계 방향의 k번째 사람이 지목당하며 마지막으로 지목된 사람은 게임에서 떠납니다.
# 3. 떠난 사람 다음 번호부터 k번째 사람을 지목합니다.
# 4. 마지막에 남은 사람이 이깁니다.

# 사람 수 n, 변수 k, return 게임의 승자

from collections import deque

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        self.queue1 = deque() # deque 정의

        for i in range(1, n+1):
            self.queue1.append(i) # deque에 n만큼의 원소를 맨 끝(오른쪽)부터 넣어줌 ex) n=5일때, 1 2 3 4 5
        
        while self.queue1:
            temp = k - 1 # k번째의 사람이 게임에서 떠나야하므로 k-1번째까지 실행
            while temp > 0:
                self.queue1.append(self.queue1.popleft()) # k-1번째까지의 원소를 deque 오른쪽에 다시 넣어줌
                temp -= 1
            result = self.queue1.popleft()

        return result
        
        # k-1번째까지의 원소를 deque 오른쪽에 다시 넣어줌 
        # ex) n=5, k=2인 경우
        #     1 2 3 4 5
        #     2 3 4 5 1 temp = 0 이므로 2를 deque에서 뺌
        #     3 4 5 1   temp = 1
        #     4 5 1 3   temp = 0 이므로 4를 deque에서 뺌
        #     5 1 3     temp = 1
        #     1 3 5     temp = 0 이므로 1를 deque에서 뺌
        #     3 5       temp = 1
        #     5 3       temp = 0 이므로 5를 deque에서 뺌
        #     3         result = 3
