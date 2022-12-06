obstacleGrid = [[0,0,0],[0,1,1],[0,1,0]]

DP = [[0 for j in range(len(obstacleGrid[0]))] for i in range(len(obstacleGrid))]

# 开始填表

def pick(x, y):
    if x < 0 or y < 0 or x == len(obstacleGrid) or y ==len(obstacleGrid[0]) or obstacleGrid[x][y] == 1:
        return 0
    return DP[x][y]
f = 1
for i in range(len(obstacleGrid) - 1, -1, -1):
    for j in range(len(obstacleGrid[0]) - 1, -1, -1):
        if f == 1:
            DP[-1][-1] = 1
            f = 0
            continue
        DP[i][j] = pick(i + 1, j) + pick(i, j + 1)

print(DP[0][0])
        







