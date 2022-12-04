# 给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。
# 一旦你支付此费用，即可选择向上爬一个或者两个台阶。
# 你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。
# 请你计算并返回达到楼梯顶部的最低花费。

cost = [1,100,1,1,1,100,1,1,100,1]

# def tryFunc(now):
#     if now >= len(cost):
#         return 0
    
#     if now == -1:
#         return  min(tryFunc(now + 1), tryFunc(now + 2))
#     p1 = cost[now] + tryFunc(now + 1)
#     p2 = cost[now] + tryFunc(now + 2)
#     return min(p1, p2)
# print(tryFunc(-1))

DP = [0 for _ in range(len(cost) + 2)]
DP[-1] = DP[-2] = 0

for i in range(len(DP) - 3, -1, -1):
    DP[i] = min(DP[i + 1], DP[i + 2]) + cost[i]

print(min(DP[0], DP[1]))

