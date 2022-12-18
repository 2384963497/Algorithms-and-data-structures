# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         if headA == None or headB == None:
#             return None
#         nodeA = headA
#         nodeB = headB
        
#         lenA = 1
#         while nodeA.next != None:
#             nodeA = nodeA.next
#             lenA += 1
        

#         lenB = 1
#         while nodeB.next != None:
#             nodeB = nodeB.next
#             lenB += 1
        
#         if nodeA != nodeB:
#             return None
#         if lenA > lenB:
#             nodeA = headA
#             for i in range(lenA - lenB):
#                 nodeA = nodeA.next
#             nodeB = headB
#         else:
#             nodeB = headB
#             for i in range(lenB - lenA):
#                 nodeB = nodeB.next
#             nodeA = headA
        
#         while nodeA != nodeB:
#             nodeA = nodeA.next
#             nodeB = nodeB.next
#         return nodeA

#############################################################
# 方法2
# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         if headA == None or headB == None:
#             return None
#         nodeA = headA
#         nodeB = headB
        
#         while nodeA != nodeB:
#             if nodeA != None:
#                 nodeA = nodeA.next
#             else:
#                 nodeA = headB
            
#             if nodeB != None:
#                 nodeB = nodeB.next
#             else:
#                 nodeB = headA
#         return nodeA


