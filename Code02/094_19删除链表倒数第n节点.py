# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         if head.next == None:
#             head = None
#             return head
#         # 以下情况均为大于等于二节点的情况
#         end = head
#         for i in range(n):
#             end = end.next
        
#         cur = head
#         while end != None:
#             pre = cur 
#             cur = cur.next
#             end = end.next
#         if cur == head:
#             head = head.next
#         else:
#             pre.next = cur.next
#         return head
        