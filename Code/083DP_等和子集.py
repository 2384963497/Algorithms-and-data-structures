

# def tryFunc(nowList,now):
#     if now == len(nums):
#         return False
#     if nowList != None and sum(nowList) * 2 == sum(nums):
#         return True
    
#     # 要当前数
#     r1 = tryFunc(nowList, now + 1)
#     # 不要当前数
#     r2 = tryFunc(nowList + [nums[now]], now + 1)
#     return r1 or r2

# print(tryFunc([], 0))

nums = [1,5,11,5]
target = sum(nums)
if target % 2 == 1:
    # 总和为奇数，绝不可能分割出两个等和子集
    # return False
    print(False)

target //= 2
DP = [[False for t in range(target + 1)] for i in nums]
for i in range(len(nums)):
    DP[i][0] = True

for j in range(1, target + 1):
    # 最后一行先填, 只能组成原位置的值
    if nums[-1] == j:
        DP[-1][j] = True
    else:
        DP[-1][j] = False

for i in range(len(nums) - 2, -1, -1):
    for j in range(1, target + 1):
        r1 = False
        if nums[i] <= j:
            r1 = DP[i + 1][j - nums[i]]
        r2 = DP[i + 1][j]
        DP[i][j] = r1 or r2
print(DP[0][target])

# def tryFunc(nowT, now):
#     if nowT == 0:# 刚好组合出这个数
#         return True
#     if now == len(nums):
#         return False
    
#     r1 = 0
#     if nums[now] <= nowT:
#         r1 = tryFunc(nowT - nums[now], now + 1)
#     r2 = tryFunc(nowT, now + 1)
#     return r1 or r2

# print(tryFunc(target, 0))

