
bagWei = 6
bagNum = 3

w = [3, 2, 4]
v = [5, 4, 2]

count = 0
def func(nowInd, restW, restN):
    global count
    if restW < 0 or restN == 0:
        return 0
    if nowInd == len(w):
        return 0
    print(f"({nowInd}, {restW}, {restN})")
    count += 1
    
    # r1表示选择当前货物的价值
    r1 = 0
    if restW >= w[nowInd]:
        r1 = v[nowInd] + func(nowInd + 1, restW - w[nowInd], restN - 1)
    
    # r2表示不选当前货物的价值
    r2 = func(nowInd + 1, restW, restN)
    return max(r1, r2)
print(func(0, bagWei, bagNum))
print(f"{count}次\n---------------")


