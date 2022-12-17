
candidates = [2,5,2,1,2]
used = [0 for i in range(len(candidates))]
target = 5
res = []
candidates.sort()

def backTracking(nowInd, path):
    if sum(path) == target:
        res.append(path[:])
        return
    if nowInd == len(candidates):
        return
    
    for i in range(nowInd, len(candidates)):
        if i > 0 and candidates[i] == candidates[i - 1] and used[i - 1] == 0:
            continue
        path.append(candidates[i])
        used[i] = 1
        if sum(path) > target:
            path.pop()
            return
        backTracking(i + 1, path)
        path.pop()
        used[i] = 0

backTracking(0, [])
print(res)
