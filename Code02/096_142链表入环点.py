# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head == None or head.next == None:
#             return None
#         fast = slow = head
#         flag = False
        
#         while fast != None:
#             fast = fast.next
#             if fast != None:
#                 fast = fast.next
#             slow = slow.next
#             if slow == fast:
#                 flag = True
#                 break
            
#         if flag == False:
#             return None
#         fast = head
#         while fast != slow:
#             fast = fast.next
#             slow = slow.next
#         return fast





        