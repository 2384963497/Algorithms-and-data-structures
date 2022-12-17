# 棋盘横线9  竖线10
x = 7
y = 7
k = 10

# DP数组初始化
DP = {}
for i in range(k + 1):
    DP[i] = []
DP[0].append([0, 0])

# 填写过程
m = 1
while m <= k:
    for i in DP[m - 1]: 
        if i[0] < 0 or i[0] > 8 or i[1] < 0 or i[1] > 9:    # 越界的情况
            continue
        else:
            DP[m].append([i[0] + 2, i[1] + 1])
            DP[m].append([i[0] + 2, i[1] - 1])
            DP[m].append([i[0] - 2, i[1] + 1])
            DP[m].append([i[0] - 2, i[1] - 1])
            
            DP[m].append([i[0] + 1, i[1] + 2])
            DP[m].append([i[0] + 1, i[1] - 2])
            DP[m].append([i[0] - 1, i[1] + 2])
            DP[m].append([i[0] - 1, i[1] - 2])
    m += 1
# m = 1
# while m <= k:
#     for i in DP[m - 1]:
#         # 当前点上面的情况
#         if 0 <= i[0] - 2 <= 8:  # 上面有至少2行
#             if 0 <= i[1] - 1 <= 9:  # 左边有至少1列
#                 DP[m].append([i[0] - 2, i[1] - 1])
#             if 0 <= i[1] + 1 <= 9:
#                 DP[m].append([i[0] - 2, i[1] + 1])

#             if 0 <= i[1] + 2 <= 9:  # 左边有至少2列
#                 DP[m].append([i[0] - 1, i[1] + 2])
#             if 0 <= i[1] - 2 <= 9:
#                 DP[m].append([i[0] - 1, i[1] - 2])

#         elif 0 <= i[0] - 1 <= 8:  # 上面有至少1行
#             if 0 <= i[1] - 2 <= 9:  # 左边有至少2列
#                 DP[m].append([i[0] - 1, i[1] - 2])
#             if 0 <= i[1] + 2 <= 9:
#                 DP[m].append([i[0] - 1, i[1] + 2])
#         # 当前点下面的情况
#         if 0 <= i[0] + 2 <= 8:  # 上面有至少2行
#             if 0 <= i[1] - 1 <= 9:  # 左边有至少1列
#                 DP[m].append([i[0] + 2, i[1] - 1])
#             if 0 <= i[1] + 1 <= 9:
#                 DP[m].append([i[0] + 2, i[1] + 1])

#             if 0 <= i[1] + 2 <= 9:  # 左边有至少2列
#                 DP[m].append([i[0] + 1, i[1] + 2])
#             if 0 <= i[1] - 2 <= 9:
#                 DP[m].append([i[0] + 1, i[1] - 2])

#         elif 0 <= i[0] + 1 <= 8:  # 上面有至少1行
#             if 0 <= i[1] - 2 <= 9:  # 左边有至少2列
#                 DP[m].append([i[0] + 1, i[1] - 2])
#             if 0 <= i[1] + 2 <= 9:
#                 DP[m].append([i[0] + 1, i[1] + 2])
#     m += 1

count = 0
for i in DP[k]:
    if [x, y] == i:
        count += 1

print(count)








