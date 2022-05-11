# leetcode 617

# 두 개의 이진트리 root1, root2가 주어짐
# 두 개의 이진트리를 서로 겹치게 하면 어떤 노드는 겹쳐질 것이고, 어떤 것들은 겹쳐지지 않을텐데
# 겹쳐지는 노드는 각 노드 값을 더하고 겹쳐지지 않는 노드는 그대로 적음
# 이 과정에서 새로운 이진 트리가 만들어짐

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]: # root1과 root2를 더해주는 함수 정의
        
        if root1==None:  # root1이 null이면 root2를 반환
            return root2
        elif root2==None:  # root2가 null이면 root1를 반환
            return root1
        
        elif root1!=None and root2!=None: # root1과 root2가 null이 아닐 때, root1과 root2의 value와 구조를 합쳐줌
            
            root1.left=self.mergeTrees(root1.left, root2.left)
            root1.right=self.mergeTrees(root1.right, root2.right)
            root1.val=root1.val + root2.val

            return root1
