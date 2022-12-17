coins = [2, 4]
amount = 7

DP = [-1 for j in range(amount + 1)]
DP[0] = 0

for j in range(1, amount + 1):
    for i in coins:
        if i <= j and DP[j - i] != -1:
            if DP[j] == -1 or DP[j - i] + 1 < DP[j]:
                DP[j] = DP[j - i] + 1
                
print(DP[amount])
# return DP[amount]



