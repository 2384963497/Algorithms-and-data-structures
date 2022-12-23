# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head.next == None:	
#             return head
#         slow = fast = head
#         while fast and fast.next != None:
#             fast = fast.next.next
#             slow = slow.next
            
#         return slow