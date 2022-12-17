# 记忆存储
N = 4
S = 2
A = 4
K = 4
# 申请一个记录表; 表的列表示步数 [0, K], 行表示起点 范围[1, N]
# -1表示该单元格没有被处理过
tMap = [[-1 for i in range(K + 1)] for j in range(N)]

global count
count = 0
def func(N, S, K, A):
    global count
    if tMap[S - 1][K] != -1:
        return tMap[S - 1][K]
    # 以下代码是在该点没有处理过的情况下处理的
    print(f"({S}, {K})")
    count += 1
    res = 0
    if K == 0:
        if S == A:
            res = 1
    elif S == 1:
        res = func(N, 2, K - 1, A)
    elif S == N:
        res = func(N, N - 1, K - 1, A)
    else:
        res = func(N, S - 1, K - 1, A) + func(N, S + 1, K - 1, A)
    tMap[S - 1][K] = res
    return res
    
func(N, S, K, A)
print(f"{'=' * 20}\n共{tMap[S - 1][K]}种走法")
print(f"总处理次数:{count}")




