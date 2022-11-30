
bagWei = 6
bagNum = 3

temp = []
w = [3, 2, 4]
v = [5, 4, 2]

def DFS(nowInd, nowWei, nowNum, nowVal):
    if nowWei > bagWei or nowNum > bagNum:
        return
    temp.append(nowVal)
    
    for i in range(nowInd, len(w)):
        DFS(i + 1, nowWei + w[i], nowNum + 1, nowVal + v[i])

DFS(0, 0, 0, 0)

res = max(temp)
print(res)





