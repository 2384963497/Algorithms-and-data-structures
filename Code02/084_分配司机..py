income = [[10, 202], [25, 110], [5, 10], [5, 100]]

def maxMoney(now, restA):
    if now == len(income):
        return 0
    
    # A先满了
    if restA == 0:
        # 只能去B
        return maxMoney(now + 1, restA) + income[now][1]
    
    # B先满了
    if len(income) - now == restA:
        # 只能去A了
        return maxMoney(now + 1, restA - 1) + income[now][0]
    
    # 否则可以自由选择去A或者B
    p1 = maxMoney(now + 1, restA) + income[now][1]
    p2 = maxMoney(now + 1, restA - 1) + income[now][0]
    return max(p1, p2)
memo = dict()
def maxMoney1(now, restA):
    if memo.get(str(now) + '_' + str(restA)) != None:
        return memo[str(now) + '_' + str(restA)]
    if now == len(income):
        return 0
    
    # A先满了
    if restA == 0:
        # 只能去B
        return maxMoney(now + 1, restA) + income[now][1]
    
    # B先满了
    if len(income) - now == restA:
        # 只能去A了
        return maxMoney(now + 1, restA - 1) + income[now][0]
    
    # 否则可以自由选择去A或者B
    p1 = maxMoney(now + 1, restA) + income[now][1]
    p2 = maxMoney(now + 1, restA - 1) + income[now][0]
    memo[str(now) + '_' + str(restA)] = max(p1, p2)
    return memo[str(now) + '_' + str(restA)]
restA = len(income) // 2
res1 = maxMoney(0, restA)
res2 = maxMoney1(0, restA)
print(res1, res2)

