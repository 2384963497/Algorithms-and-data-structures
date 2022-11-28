
nums = [1,2,3]
res = []


def DFS(path):
    if len(path) == len(nums):
        res.append(path[:])
        return
    for i in range(len(nums)):
        if nums[i] in path:
            continue
        DFS(path + [nums[i]])

DFS([])
print(res)




