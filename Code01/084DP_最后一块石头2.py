
stones = [2,7,4,1,8,1]
# 解题思路； 分成尽量重量相等的两堆石头；他们的差值就是最小
target = sum(stones) // 2

# 从石头中尽量拼凑出于target相近的值
DP = [False for j in range(target + 1)]
DP[0] = True

i = len(stones) - 1
if stones[-1] <= target:
    DP[stones[-1]] = True

temp = DP[:]
i -= 1
while i >= 0:
    for j in range(1, target + 1):
        r1 = False
        if stones[i] <= j:
            r1 = temp[j - stones[i]]
        r2 = temp[j]
        DP[j] = r1 or r2
    i -= 1
    temp = DP[:]

for i in range(len(DP) - 1, -1, -1):
    if DP[i]:
        break





