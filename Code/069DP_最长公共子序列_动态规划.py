text1 = "abc"
text2 = "def" 

DP = [[-1 for y in range(len(text2))] for x in range(len(text1))]
DP[0][0] = 1 if text1[0] == text2[0] else 0
for y in range(1, len(text2)):
    if text1[0] == text2[y]:
        DP[0][y] = 1
    else:
        DP[0][y] = DP[0][y - 1]
for x in range(1, len(text1)):
    if text2[0] == text1[x]:
        DP[x][0] = 1
    else:
        DP[x][0] = DP[x - 1][0]

# 普遍位置依赖
for x in range(1, len(text1)):
    for y in range(1, len(text2)):
        r1 = 0
        if text1[x] == text2[y]:
            DP[x][y] = DP[x - 1][y - 1] + 1
            continue    # 如果两字符串末尾相同 那么该种模型下的子串最长
        r2 = DP[x - 1][y]
        r3 = DP[x][y - 1]
        DP[x][y] = max(r1, r2, r3)

print(DP[len(text1) - 1][len(text2) - 1])
