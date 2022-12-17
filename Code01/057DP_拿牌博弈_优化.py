# 存储

pokers = [5, 7, 4, 5, 8, 1, 6, 0, 3, 4, 1, 7]
N = len(pokers) - 1

# 生成两张记录表；分别记录先手的每个起点到终点的最优选择值,后手表同理
# 表的长和宽都是[0, N]
fMap = [[-1 for i in range(N + 1)] for j in range(N + 1)]
sMap = [[-1 for i in range(N + 1)] for j in range(N + 1)]

def fFunc(L, R):
    if fMap[L][R] != -1:
        return fMap[L][R]
    
    # 以下代码为当前单元格没有处理过时处理步骤
    if L == R:
        res = pokers[L]
    else:
        p1 = pokers[L] + sFunc(L + 1, R)
        p2 = pokers[R] + sFunc(L, R - 1)
        res = max(p1, p2)
    fMap[L][R] = res
    return res

def sFunc(L, R):
    if sMap[L][R] != -1:
        return sMap[L][R]
    
    if L == R:
        res = 0
    else:
        r1 = fFunc(L + 1, R)
        r2 = fFunc(L, R - 1)
        res = min(r1, r2)

    sMap[L][R] = res
    return res

fPlayerScore = fFunc(0, len(pokers) - 1)
sPlayerScore = sum(pokers) - fPlayerScore

print(f"先手玩家的最优分数为:{fPlayerScore}\n后手玩家的最优分数为:{sPlayerScore}")
















