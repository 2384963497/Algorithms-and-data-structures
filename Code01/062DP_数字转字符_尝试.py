# string = '7210231231232031203123'
string = '110'

def tryFunc(nowInd):
    if nowInd == len(string):
        return 1
    
    if string[nowInd] == '0':
        return 0
    r1 = tryFunc(nowInd + 1)
    r2 = 0
    if nowInd != len(string)-1 and int(string[nowInd:nowInd + 2]) <= 26:
        r2 = tryFunc(nowInd + 2)
    return r1 + r2
print(tryFunc(0))

