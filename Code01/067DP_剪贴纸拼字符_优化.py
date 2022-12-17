target = "stoodcrease"
stickers = ["control","heart","interest","stream","sentence","soil","wonder","them","month","slip","table","miss","boat","speak","figure","no","perhaps","twenty","throw","rich","capital","save","method","store","meant","life","oil","string","song","food","am","who","fat","if","put","path","come","grow","box","great","word","object","stead","common","fresh","the","operate","where","road","mean"]
# target = "thehat"
# stickers = ["with","example","science"]

tMap = {}

def minus(s, sticker):
    temp = {}
    for i in s:
        temp[i] = temp.get(i, 0) + 1
    for i in sticker:
        if temp.get(i) != None:
            temp[i] -= 1
    tempS = ""
    for i in temp:
        if temp[i] > 0:
            tempS += i * temp[i]
    return tempS


def DFS(nowStr):
    if nowStr == "":
        return 0
    
    if tMap.get(nowStr) != None:
        return tMap[nowStr]

    counts = []
    for i in stickers:
        tempStr = nowStr
        if nowStr[0] in i:
            tempStr = minus(tempStr, i)

            deep = DFS(tempStr)
            if deep == -1:
                return -1
            else:
                counts.append(deep + 1)

    if counts == []:
        return -1
    else:
        tMap[nowStr] = min(counts)
        return tMap[nowStr]

flag = DFS(target)
if flag == -1:
    print(-1)
else:
    print(tMap[target])






