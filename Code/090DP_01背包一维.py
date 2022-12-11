bagWei = 15

w = [3, 2, 4, 7, 3, 1, 7]
v = [5, 6, 3, 19, 12, 100, 2]

DP = [0 for _ in range(bagWei + 1)]

for i in range(len(w)):
    for j in range(bagWei, w[i] - 1, -1):
        DP[j] = max(v[i] + DP[j - w[i]], DP[j])


print(DP[-1])

