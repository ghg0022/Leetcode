# leetcode 104

# 주어진 이진 트리의 최대 깊이를 구하시오
# 이진 트리의 최대 깊이는 root noode에서 leaf node까지 가장 긴 경로의 노드 수이다

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root: # node가 없는 경우 0을 반환
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1 
        
        # 재귀방식으로 트리 좌우의 깊이를 구하는 함수를 호출하고 
        # 트리 좌우의 깊이 값을 비교, 이 중 큰 값을 구한 다음
        # 구한 값에 1을 더해주면 깊이를 구하는 함수를 호출할 때마다 1이 더해지게 되어서 깊이를 구할 수 있음
