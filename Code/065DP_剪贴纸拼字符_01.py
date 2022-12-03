target = "atomher"
stickers = ["these","guess","about","garden","him"]


def DFS(nowStr):
    if nowStr == '':
        return 0
    
    counts = []
    for i in stickers:
        tempStr = nowStr
        for j in i:
            tempStr = tempStr.replace(j, '', 1)
        minusLen = len(nowStr) - len(tempStr)
        if minusLen == 0:
            continue
        
        next = DFS(tempStr)
        if next == -1:# 下一层走不通
            continue
        else:
            counts.append(next + 1)

    if counts == []:
        return -1
    else:
        return min(counts)


print(DFS(target))
    





