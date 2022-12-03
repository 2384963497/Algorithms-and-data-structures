N = 4
S = 2
A = 4
K = 4
# 初始化一张记录表；表的列表示步数 [0, K], 行表示起点 范围[1, N]
tMap = [[0 for i in range(K + 1)] for j in range(N)]

# 初始化第一列的数据; 除了 A 行的单元格为1其余行为0; 
# 对应代码
    # if K == 0:
    #     if S == A:
    #         res = 1
tMap[A - 1][0] = 1

# 开始填剩余单元格
for j in range(1, K + 1):
    # 单元格依赖: 
    # 第一行的单元格依赖左下角的单元格
    # 对应代码
        # if S == 1:
        #   return func(N, 2, K - 1, A)
    # 最后一行的单元格依赖为左上角的单元格
    # 对应代码
        # elif S == N:
        #   return func(N, S - 1, K - 1, A)
    # 其余行单元格的依赖为当前单元格的左上角和左下角的和
    # 对应代码
        # return func(N, S - 1, K - 1, A) + func(N, S + 1, K - 1, A)
    tMap[0][j] = tMap[1][j - 1]
    for i in range(1, N - 1):
        tMap[i][j] = tMap[i - 1][j - 1] + tMap[i + 1][j - 1]
    tMap[N - 1][j] = tMap[N - 2][j - 1]

print(tMap[S - 1][K])