# arr = [1, 2, 4]
def DPfunc(arr):
    left = min(arr)
    right = sum(arr)

    DP = [[False for j in range(right + 1)] for i in range(len(arr))]
    DP[0][0] = DP[0][arr[0]] = True

    for i in range(1, len(arr)):
        DP[i][0] = True
        for j in range(1, right + 1):
            DP[i][j] = DP[i - 1][j] or (DP[i - 1][j - arr[i]] if j - arr[i] >= 0 else False)
    for j in range(left + 1, right + 1):
        if DP[-1][j] == False:
            return j
    
    return right + 1

def rangeFunc(arr):
    arr.sort()
    area = 1

    for i in arr[1:]:
        if i < area + 1:
            # 合法
            area += i
        else:
            return area + 1
    return area + 1

import random
time = 1000
for i in range(time):
    l = []
    length = 10
    for j in range(length):
        l.append(random.randint(1, 15))
        l.append(1)
    if DPfunc(l) != rangeFunc(l):
        break
if i == time - 1:
    print("success！")
else:
    print("fucked!")
    


