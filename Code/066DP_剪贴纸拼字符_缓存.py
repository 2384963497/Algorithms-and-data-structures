target = "stoodcrease"
stickers = ["control","heart","interest","stream","sentence","soil","wonder","them","month","slip","table","miss","boat","speak","figure","no","perhaps","twenty","throw","rich","capital","save","method","store","meant","life","oil","string","song","food","am","who","fat","if","put","path","come","grow","box","great","word","object","stead","common","fresh","the","operate","where","road","mean"]
# target = "thehat"
# stickers = ["with","example","science"]

tMap = {}
def DFS(nowStr):
    if nowStr == '':
        return 0

    if tMap.get(nowStr) != None:
        return tMap[nowStr]
    
    counts = []
    for i in stickers:
        tempStr = nowStr
        for j in i:
            tempStr = tempStr.replace(j, '', 1)
        
        if len(tempStr) != len(nowStr): # 当前贴纸能有效的拼出原字符的一部分
            next = DFS(tempStr) # 获取它下面的情况 看该节点往下是否能走通
            if next == -1:  # 走该条路径往下走不通
                tMap[nowStr] = - 1
                return tMap[nowStr] # 同一层的其他贴纸也不需要继续试下去了
            else:
                counts.append(next + 1) # 走该条路径拼出当前状态的其中一条路径的高度
    if counts == []:    # 证明在所有贴纸中都拼不出当期字符串
        tMap[nowStr] = - 1
        return tMap[nowStr]
    else:
        tMap[nowStr] = min(counts)
        return tMap[nowStr]
DFS(target)

print(tMap[target])
    





