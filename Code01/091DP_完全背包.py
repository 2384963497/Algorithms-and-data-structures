bagWei = 15

w = [3, 2, 4, 7, 3, 1, 7]
v = [5, 6, 3, 19, 12, 5, 2]

DP = [0 for _ in range(bagWei + 1)]

# for i in range(len(w)):
#     for j in range(w[i], bagWei + 1):
#         DP[j] = max(v[i] + DP[j - w[i]], DP[j])

for j in range(bagWei + 1):
    for i in range(len(w)):
        if j >= w[i]:
            DP[j] = max(v[i] + DP[j - w[i]], DP[j])



print(DP[-1])

