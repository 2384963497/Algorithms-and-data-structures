nums = [0,0,0,0,1]
# nums = [1, 0]
target = 1
# nums = [1,1,1,1,1]
# target = 3
t = sum(nums)
DP = [[0 for j in range(-t, t + 1)] for i in nums]

# 处理最后一行
line = nums[-1]
i = len(nums) - 1
if nums[-1] == 0:
    DP[i][0 + t] = 2
else:
    DP[i][t + nums[-1]] = 1
    DP[i][t - nums[-1]] = 1

# 普遍位置
i -= 1
while i >= 0:
    line += nums[i]
    for j in range(-line ,line + 1):
        if j + t - nums[i] >= 0:
            r1 = DP[i + 1][j + t - nums[i]]
        else:
            r1 = 0
        if j + t + nums[i] <= 2 * t:
            r2 = DP[i + 1][j + t + nums[i]]
        else:
            r2 = 0
        DP[i][j + t] = r1 + r2
    i -= 1

print(DP[0][t - target])
# def func(now, nowT):
#     if now == len(nums) - 1:
#         if nums[-1] == 0 and nums[-1] == nowT:
#             return 2
#         if nums[-1] == nowT or nums[-1] == -nowT:
#             return 1 
#         else:
#             return 0
    
#     r1 = func(now + 1, nowT - nums[now])
#     r2 = func(now + 1, nowT + nums[now])
#     return r1 + r2

# return func(0, target)
