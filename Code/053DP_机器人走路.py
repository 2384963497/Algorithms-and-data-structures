# 假设有排成一行的N个位置，记为1~N，N一定大于或等于2开始时机器人在其中的S位置上(S一定是1~N中的一个)
# 如果机器人来到1位置，那么下一步只能往右来到2位置﹔
# 如果机器人来到N位置，那么下一步只能往左来到N-1位置;
# 如果机器人来到中间位置，那么下一步可以往左走或者往右走;
# 规定机器人必须走K步，最终能来到A位置(A也是1~N中的一个)的方法有多少种给定四个参数N、S、K、A，返回方法数。

count = 0
def func(N, S, K, A):
    global count
    '''
    N : 可以走动地范围
    S : 当前起始点
    K : 当前剩余的步数
    A : 目的地
    '''
    # base case
    print(f"({S}, {K})")
    count += 1
    if K == 0:
        if S == A:
            return 1
        return 0 # 步数为0时 只有起点和终点重合才有一种方式.
    
    if S == 1:
        return func(N, 2, K - 1, A)
    elif S == N:
        return func(N, S - 1, K - 1, A)
    else:
        return func(N, S - 1, K - 1, A) + func(N, S + 1, K - 1, A)

print(f"{'=' * 20}\n共{func(4, 2, 4, 4)}种走法")
print(f"总处理次数:{count}")