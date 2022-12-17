# string = '7210231231232031203123'
# string = "111111111111111111111111111111111111111111111"
string = "305"

tMap = [-1 for _ in range(len(string))]

def tryFunc(nowInd):

    if nowInd == len(string):
        return 1

    if tMap[nowInd] != -1:
        return tMap[nowInd]
    
    if string[nowInd] == '0':
        tMap[nowInd] = 0
        return tMap[nowInd]
    
    r1 = tryFunc(nowInd + 1)
    r2 = 0
    if nowInd != len(string)-1 and int(string[nowInd:nowInd + 2]) <= 26:
        r2 = tryFunc(nowInd + 2)
    
    tMap[nowInd] = r1 + r2
    return tMap[nowInd]
print(tryFunc(0))
