n = 10
# if n <= 3:
#     return n - 1
DP = [0 for i in range(n + 1)]

DP[2] = 2
DP[3] = 3

for i in range(4, n + 1):
    temp = []
    for j in range(2, i // 2 + 1):
        temp.append(j * DP[i - j])
    DP[i] = max(temp)


# return DP[n]


print(DP[n])