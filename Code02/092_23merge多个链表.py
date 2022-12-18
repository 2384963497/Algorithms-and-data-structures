# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         def mergeTwoLists(list1, list2):
#             if list1 == None:
#                 return list2
#             elif list2 == None:
#                 return list1
            
#             cur1 = list1
#             cur2 = list2

#             if cur1.val < cur2.val:
#                 newHead = cur1
#                 cur1 = cur1.next
#             else:
#                 newHead = cur2
#                 cur2 = cur2.next

#             curNew = newHead
#             while cur1 and cur2:
#                 if cur1.val < cur2.val:
#                     curNew.next = cur1
#                     cur1 = cur1.next
#                 else:
#                     curNew.next = cur2
#                     cur2 = cur2.next
#                 curNew = curNew.next
            
#             curNew.next = cur1 if cur1 != None else cur2
#             return newHead

#         if len(lists) == 0:
#             return None

#         while len(lists) != 1:
#             a = lists.pop()
#             b = lists.pop()
#             lists.append(mergeTwoLists(a, b))
#         return lists[0]


# class Solution:
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         if len(lists) == 0:
#             return None

#         import heapq
        
#         h = []
#         for i in lists:
#             if i:
#                 j = i
#                 while j:
#                     heapq.heappush(h, j.val)
#                     j = j.next
                
#         res = ListNode()
#         cur = res
#         while len(h) != 0:
#                 temp = ListNode(heapq.heappop(h))
#                 cur.next = temp
#                 cur = cur.next

#         return res.next