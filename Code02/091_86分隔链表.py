# class Solution:
#     def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
#         if head == None:
#             return head

#         big = ListNode()
#         bigp = big
#         small = ListNode()
#         smallp = small

#         cur = head
#         while cur != None:
#             if cur.val < x:
#                 smallp.next = cur
#                 cur = cur.next
#                 smallp = smallp.next
#                 smallp.next = None
#             else:
#                 bigp.next = cur
#                 cur = cur.next
#                 bigp = bigp.next
#                 bigp.next = None
        
#         smallp.next = big.next

#         return small.next