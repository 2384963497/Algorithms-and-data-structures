amount = 5
coins = [1, 2, 5]






def DFS(nowI, nowA):
    if nowA == 0:
        return 1
    if nowA < 0:
        return 0
    
    count = 0
    for i in range(nowI, len(coins)):
        count += DFS(i, nowA - coins[i])
    return count

# return DFS(0, amount)




