m = 7
n = 3

# if m <= 1 and n <= 1:
#     return 0

# def tryFunc(nowX, nowY):
#     if nowX == m or nowY == n:
#         return 0

#     if nowX == m - 1 and nowY == n - 1:
#         return 1
    
#     return tryFunc(nowX + 1, nowY) + tryFunc(nowX, nowY + 1)
# print(tryFunc(0, 0))

DP = [[0 for j in range(n)] for i in range(m)]
DP[m - 1][n - 1] = 1

def get(x, y):
    if x == m or y == n:
        return 0
    return DP[x][y]

for i in range(m - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        if i == m - 1 and j == n - 1:   # 跳过右下角的格子开始填值
            continue
        DP[i][j] = get(i + 1, j) + get(i, j + 1)

print(DP[0][0])






