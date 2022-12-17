# 棋盘横线10  竖线9
x = 8
y = 6
k = 10

DP = [[[0 for j in range(9)] for i in range(10)] for z in range(k + 1)]
DP[0][x][y] = 1


def pick(z, x, y):
    if x < 0 or x > 9 or y < 0 or y > 8:
        return 0
    return DP[z][x][y]

for z in range(1, k + 1):
    for i in range(10):
        for j in range(9):
            DP[z][i][j] += pick(z - 1, i + 2, j + 1)
            DP[z][i][j] += pick(z - 1, i + 2, j - 1)
            DP[z][i][j] += pick(z - 1, i - 2, j + 1)
            DP[z][i][j] += pick(z - 1, i - 2, j - 1)

            DP[z][i][j] += pick(z - 1, i + 1, j + 2)
            DP[z][i][j] += pick(z - 1, i + 1, j - 2)
            DP[z][i][j] += pick(z - 1, i - 1, j + 2)
            DP[z][i][j] += pick(z - 1, i - 1, j - 2)
            
    
print(DP[k][0][0])


