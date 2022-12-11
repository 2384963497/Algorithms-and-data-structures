nums = [1,2,3]
target = 4

def DFS(nowT):
    if nowT == 0:
        return 1
    if nowT < 0:
        return 0 
    
    count = 0
    for i in range(len(nums)):
        count += DFS(nowT - nums[i])
    return count
    
print(DFS(target))






