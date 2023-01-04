# class Solution:
#     def lengthOfLIS(self, nums: List[int]) -> int:
#         if len(nums) <= 1:
#             return 1
#         DP = [1 for i in nums]
        
#         for i in range(1,len(nums)):
#             temp = []
#             for j in range(i - 1, -1, -1):
#                 if nums[j] < nums[i]:
#                     temp.append(DP[j] + 1)
#             if temp != []:
#                 DP[i] = max(temp)
            

#         return max(DP)
l1 = [[2,3], [5,2], [6,1]]
print(l1)
l1.sort(key = lambda x:-x[0])
print(l1)