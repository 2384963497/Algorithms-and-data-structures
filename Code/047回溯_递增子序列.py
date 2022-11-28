
nums = [1,2,3,4,5,6,7,8,9,10,1,1,1,1,1]
res = []
def DFS(nowInd, path):
    if len(path) > 1:
        res.append(path[:])
    
    for i in range(nowInd, len(nums)):
        if i > nowInd and nums[i] in nums[nowInd:i]:
            continue
        if len(path) == 0 or nums[i] >= path[-1]:
            DFS(i + 1, path + [nums[i]])

DFS(0, [])
print(len(res))
