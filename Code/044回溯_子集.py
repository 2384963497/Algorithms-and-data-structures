

# nums = [0, 1, 2, 3]
# nums = [0]
nums = [1, 2, 3]
res = []

def backTracking(startIndex, path):
    res.append(path[:])
    for i in range(startIndex, len(nums)):
        path.append(nums[i])
        backTracking(i + 1, path)
        path.pop()


backTracking(0, [])
print(res)


