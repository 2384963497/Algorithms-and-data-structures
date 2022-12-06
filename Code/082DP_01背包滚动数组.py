bagWei = 15

w = [3, 2, 4, 7, 3, 1, 7]
v = [5, 6, 3, 19, 12, 4, 2]

# def tryFunc(nowInd, nowWei):
#     if nowWei < 0 or nowInd == len(w):
#         return 0
#     r1 = 0
#     if nowWei >= w[nowInd]:
#         r1 = v[nowInd] + tryFunc(nowInd + 1, nowWei - w[nowInd])
#     r2 = tryFunc(nowInd + 1, nowWei)
#     return max(r1, r2)

# print(tryFunc(0, bagWei))

DP = [0 for j in range(bagWei + 1)]
temp = []

# 先生成最后一行
i = len(w) - 1
for j in range(bagWei + 1):
    if j >= w[i]:
        DP[j] = v[i]
    else:
        DP[j] = 0

i -= 1
temp = DP[:]
while i >= 0:
    for j in range(bagWei + 1):
        r1 = 0
        if j >= w[i]:
            r1 = v[i] + temp[j - w[i]]
        r2 = temp[j]
        DP[j] = max(r1, r2)
    temp = DP[:]
    i -= 1
print(DP[-1])

