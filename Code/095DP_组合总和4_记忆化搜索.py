nums = [1,2,3]
target = 4

tMap = {}
def DFS(nowT):
    if tMap.get(nowT) != None:
        return tMap[nowT]

    if nowT == 0:
        tMap[nowT] = 1
        return tMap[nowT]
    if nowT < 0:
        return 0 
    
    count = 0
    for i in range(len(nums)):
        count += DFS(nowT - nums[i])
    tMap[nowT] = count
    return tMap[nowT]

DFS(target)
print(tMap[target])
# return tMap[target]






