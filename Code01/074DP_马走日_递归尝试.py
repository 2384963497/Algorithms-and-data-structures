# 棋盘横线10  竖线9
x = 8
y = 6
k = 10

def tryFunc(nowX, nowY, rest):
    if nowX < 0 or nowX > 9 or nowY < 0 or nowY > 8:
        return 0
    if nowX == x and nowY == y and rest == 0:
        return 1
    if rest == 0:
        return 0

    t1 = tryFunc(nowX + 2, nowY - 1, rest - 1)
    t2 = tryFunc(nowX + 2, nowY + 1, rest - 1)
    t3 = tryFunc(nowX - 2, nowY - 1, rest - 1)
    t4 = tryFunc(nowX - 2, nowY + 1, rest - 1)
    t5 = tryFunc(nowX + 1, nowY - 2, rest - 1)
    t6 = tryFunc(nowX + 1, nowY + 2, rest - 1)
    t7 = tryFunc(nowX - 1, nowY - 2, rest - 1)
    t8 = tryFunc(nowX - 1, nowY + 2, rest - 1)
    return t1 + t2 + t3 + t4 + t5 + t6 + t7 + t8 
    
    
    

print(tryFunc(0, 0, k))



