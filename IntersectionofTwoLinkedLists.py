# LeetCode 160

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        
        if headA is None or headB is None:
            return None # 빈 연결리스트인지 확인
        
# headA의 마지막 노드에 도달 시, headB의 첫번째 노드와 연결
# 반대의 경우도 마찬가지로 headB의 마지막 노드에 도달 시, headA의 첫번째 노드와 연결
# headA = headB인 경우가 생긴다면 intersectionNode가 존재함
# ex) 4 1 8 4 5   5 6 1 8 4 5
#     5 6 1 8 4 5   4 1 8 4 5   // 값이 1인 노드의 포인터가 가리키는 노드가 8이므로, 8이 intersectionNode

        pa, pb = headA, headB

        while pa != pb:
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa
