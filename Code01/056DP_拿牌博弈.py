# 给定一个整型数组arr，代表数值不同的纸牌排成一条线玩家A和玩家B依次拿走每张纸牌
# 规定玩家A先拿，玩家B后拿
# 但是每个玩家每次只能拿走最左或最右的纸牌玩家A和玩家B都绝顶聪明
# 请返回最后获胜者的分数。
pokers = [5, 7, 4, 5, 8, 1, 6, 0, 3, 4, 1, 7]

def fFunc(L, R):
    if L == R:
        return pokers[L]
    r1 = pokers[L] + sFunc(L + 1, R)
    r2 = pokers[R] + sFunc(L, R - 1)
    return max(r1, r2)

def sFunc(L, R):
    if L == R:
        return 0
    r1 = fFunc(L + 1, R)
    r2 = fFunc(L, R - 1)
    return min(r1, r2)

fPlayerScore = fFunc(0, len(pokers) - 1)
sPlayerScore = sum(pokers) - fPlayerScore

print(f"先手玩家的最优分数为:{fPlayerScore}\n后手玩家的最优分数为:{sPlayerScore}")
# sPlayerScore = sFunc(0, len(pokers) - 1)
# print(sPlayerScore)
