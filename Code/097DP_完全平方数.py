n = 230
DP = [-1 for _ in range(n + 1)]
DP[0] = 0

for j in range(1, n + 1):
    for i in range(1, j + 1):
        if i * i > j:
            break
        if DP[j - i * i] != -1:
            if DP[j] == -1 or DP[j] > DP[j - i * i] + 1:
                DP[j] = DP[j - i * i] + 1
# return DP[-1]
print(DP[-1])