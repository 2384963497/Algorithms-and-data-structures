# 二维存储
bagWei = 15

w = [3, 2, 4, 7, 3, 1, 7]
v = [5, 6, 3, 19, 12, 4, 2]

tMap = [[-1 for i in range(bagWei + 1)] for j in w]
# 先填最后一行
t = False
for i in range(bagWei + 1):
    if i >= w[-1]:
        t = True
    if t:
        tMap[-1][i] = v[-1]
    else:
        tMap[-1][i] = 0
# 也可以准备[0, N]高度的表，最后一行置为0 


# 填普遍行
# 普遍行的依赖是当前单元格下面的单元格和下一行左侧的某个单元格
for i in range(len(w) - 2, -1, -1):
    for j in range(bagWei + 1):
        # 判断单元格是否有拿与不拿两种选择
        if w[i] > j:
            r1 = 0
        else:
            r1 = tMap[i + 1][j - w[i]] + v[i]
        r2 = tMap[i + 1][j]
        tMap[i][j] = max(r1, r2)

print(tMap[0][bagWei])

