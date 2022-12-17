
nums = [1,2,2]
nums.sort()
res = []
def DFS(nowInd, path):
    res.append(path[:])
    
    for i in range(nowInd, len(nums)):
        if i > nowInd and nums[i] == nums[i - 1]:
            continue
        DFS(i + 1, path + [nums[i]])
    
DFS(0, [])
print(res) 

