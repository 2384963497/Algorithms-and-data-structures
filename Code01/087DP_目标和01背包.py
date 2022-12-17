
# nums = [1,1,1,1,1]
# target = 3
nums = [2,107,109,113,127,131,137,3,2,3,5,7,11,13,17,19,23,29,47,53]
target = 1000

t = sum(nums) - target
# if t % 2 == 1:
    # return 0
t = t // 2
# 现在就将问题转换为了01背包问题
# 即在nums中有多少个子集的和为t

DP = [[0 for j in range(t + 1)] for i in nums]
# 初始化第一行
DP[0][0] = 1
if nums[0] <= t:
    DP[0][nums[0]] = 1

for i in range(1, len(nums)):
    # DP[i][0] = 1
    for j in range(t + 1):
        r1 = 0
        if nums[i] <= j:
            r1 = DP[i - 1][j - nums[i]]
        r2 = DP[i - 1][j]
        DP[i][j] = r1 + r2
    i -= 1
print(DP[len(nums) - 1][t])
# def func(now, nowt):
#     if now == -1:
#         if nowt == 0:
#             return 1
#         return 0

#     r1 = 0
#     if nums[now] <= nowt:
#         r1 = func(now - 1, nowt - nums[now])
#     r2 = func(now - 1, nowt)
#     return r1 + r2
# print(func(len(nums) - 1, t))



