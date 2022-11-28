nums = [1,1,2,3]
res = []
nums.sort()
used = [0 for i in range(len(nums))]
def DFS(path):
    if len(path) == len(nums):
        res.append(path[:])
        return 
    
    for i in range(len(nums)):
        if used[i] == 1 or (i > 0 and nums[i - 1] == nums[i] and used[i - 1] == 0):
            continue
        used[i] = 1
        DFS(path + [nums[i]])
        used[i] = 0
DFS([])            