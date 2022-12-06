n = 3 

DP = [1 for _ in range(n + 1)]
DP[1] = 1
for i in range(2, n + 1):
    sum = 0 
    for j in range(1, i + 1):   # 分别计算当前数值及之前的数字做头节点的可能性
        sum += DP[j - 1] * DP[i - j]
    DP[i] = sum

print(DP[n])




