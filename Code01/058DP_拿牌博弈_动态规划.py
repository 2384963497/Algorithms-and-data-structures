pokers = [5, 7, 4, 5, 8, 1, 6, 0, 3, 4, 1, 7]
N = len(pokers) - 1

# 生成两张记录表；分别记录先手的每个起点到终点的最优选择值,后手表同理
# 表的长和宽都是[0, N]
fMap = [[-1 for i in range(N + 1)] for j in range(N + 1)]
sMap = [[-1 for i in range(N + 1)] for j in range(N + 1)]

# 开始填两张表

# 两表的左上到右下的对角线即为 L == R 的情况
    # 先手表即为poker[L]
    # 后手表即为0
for i in range(N):
    fMap[i][i] = pokers[i]
    sMap[i][i] = 0

# 其他单元格的依赖关系
    # 当L > R时无意义即对角线以下的单元格两个表都不会用到
    # 先手表中非对角线的单元格依赖是 它在后手表中的相对位置  
    # 下面的单元格与poker[L]之和  和 左边单元格与pokers[R]之和 两者的较大值
    # 对应代码
        # p1 = pokers[L] + sFunc(L + 1, R)
        # p2 = pokers[R] + sFunc(L, R - 1)
        # res = max(p1, p2)
    # 后手表同样的逻辑推得

for j in range(1, N + 1): # 从第一列开始
    col = j
    row = 0
    while col <= N:
        fMap[row][col] = max(pokers[row] + sMap[row + 1][col], pokers[col] + sMap[row][col - 1])
        sMap[row][col] = min(fMap[row + 1][col], fMap[row][col - 1])
        col += 1
        row += 1
    
print(fMap[0][N])











