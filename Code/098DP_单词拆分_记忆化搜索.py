s = "aaaaaaa"
wordDict = ["aaaa","aaa"]

tMap = {}
def DFS(beg):
    if tMap.get(s[beg:]) != None:
        return False
    if beg == len(s):
        return True
    
    for i in range(beg, len(s) + 1):
        if s[beg:i + 1] in wordDict:
            temp = DFS(i + 1)
            if temp == True:
                return True
    tMap[s[beg:]] = False
    return False
print(DFS(0))



