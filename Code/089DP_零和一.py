strs = ["0","11","1000","01","0","101","1","1","1","0","0","0","0","1","0","0110101","0","11","01","00","01111","0011","1","1000","0","11101","1","0","10","0111"]
m = 9
n = 80

tMap = {}

def func(nowI, restM, restN):
    if restN == 0 and restM == 0:
        return 0
    if nowI == len(strs):
        if restN >= 0 and restM >= 0:
            return 0
        else:
            return -100
    # 选当前贴纸
    r1 = 0
    if restM - strs[nowI].count('0') >= 0 and restN - strs[nowI].count('1') >= 0:
        # 能选当前贴纸
        r1 = 1 + func(nowI + 1, restM - strs[nowI].count('0'), restN - strs[nowI].count('1'))
    # 不选当前贴纸
    r2 = func(nowI + 1, restM, restN)
    return max(r1, r2)
print(func(0, m, n))