# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         if list1 == None:
#             return list2
#         elif list2 == None:
#             return list1
        
#         cur1 = list1
#         cur2 = list2

#         if cur1.val < cur2.val:
#             newHead = cur1
#             cur1 = cur1.next
#         else:
#             newHead = cur2
#             cur2 = cur2.next

#         curNew = newHead
#         while cur1 and cur2:
#             if cur1.val < cur2.val:
#                 curNew.next = cur1
#                 cur1 = cur1.next
#             else:
#                 curNew.next = cur2
#                 cur2 = cur2.next
#             curNew = curNew.next
        
#         curNew.next = cur1 if cur1 != None else cur2
        
#         return newHead

