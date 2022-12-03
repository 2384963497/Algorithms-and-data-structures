# 除去所取物品的数量限制
# bagNum = 3 

# 尝试代码
# bagWei = 15

# w = [3, 2, 4, 7, 3, 1, 7]
# v = [5, 6, 3, 19, 12, 4, 2]

# count = 0
# def func(nowInd, restW):
#     global count
#     # base case
#     if restW < 0 or nowInd == len(w):
#         return 0
#     print(f"({nowInd}, {restW})")
#     count += 1

#     # 用r1 和 r2 分别记录是否选择当前物品的价值
#     r1 = 0
#     if restW >= w[nowInd]:
#         r1 = v[nowInd] + func(nowInd + 1, restW - w[nowInd])
    
#     r2 = func(nowInd + 1, restW)
#     return max(r1, r2)
# print(func(0, bagWei))
# print(f"共计算处理{count}次")


# 二维存储
bagWei = 15

w = [3, 2, 4, 7, 3, 1, 7]
v = [5, 6, 3, 19, 12, 4, 2]

tMap = [[-1 for i in range(bagWei + 1)] for j in w]

count = 0
def func(nowInd, restW):
    global count
    # base case
    if restW < 0 or nowInd == len(w):
        return 0
    

    if tMap[nowInd][restW] != -1:
        return tMap[nowInd][restW]




    print(f"({nowInd}, {restW})")
    count += 1

    # 用r1 和 r2 分别记录是否选择当前物品的价值
    r1 = 0
    if restW >= w[nowInd]:
        r1 = v[nowInd] + func(nowInd + 1, restW - w[nowInd])
    
    r2 = func(nowInd + 1, restW)
    tMap[nowInd][restW] = max(r1, r2)
    return tMap[nowInd][restW]

print(func(0, bagWei))
print(f"共计算处理{count}次")

