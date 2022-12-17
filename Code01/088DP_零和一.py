
strs = ["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"]
m = 9
n = 80
# strs = ["10","0001","111001","1","0"]
# m = 5
# n = 3
# strs = ["10","0","1"]
# m = 1
# n = 1


DP = [[[0 for j in range(m + 1)] for i in range(n + 1)] for z in range(len(strs))]
# 先填最上面一层的表 strs[-1] 层
# 先正确填好最上面一层
z = len(strs) - 1
for i in range(n + 1):
    for j in range(m + 1):
        r1 = 0
        if strs[z].count('0') <= j and strs[z].count('1') <= i:
                r1 = 1
        r2 = 0
        DP[z][i][j] = max(r1, r2)

for z in range(len(strs) - 2, -1, -1):
    for i in range(n + 1):
        for j in range(m + 1):
            r1 = -1
            if strs[z].count('0') <= j and strs[z].count('1') <= i:
                r1 = DP[z + 1][i - strs[z].count('1')][j - strs[z].count('0')] + 1
            r2 = DP[z + 1][i][j]
            DP[z][i][j] = max(r1, r2)
        


print(DP[0][n][m])
a = 1

# def func(nowI, restM, restN):
#     if restN == 0 and restM == 0:
#         return 0
#     if nowI == len(strs):
#         if restN >= 0 and restM >= 0:
#             return 0
#         else:
#             return -100
#     # 选当前贴纸
#     r1 = 0
#     if restM - strs[nowI].count('0') >= 0 and restN - strs[nowI].count('1') >= 0:
#         # 能选当前贴纸
#         r1 = 1 + func(nowI + 1, restM - strs[nowI].count('0'), restN - strs[nowI].count('1'))
#     # 不选当前贴纸
#     r2 = func(nowI + 1, restM, restN)
#     return max(r1, r2)
# print(func(0, m, n))
        


