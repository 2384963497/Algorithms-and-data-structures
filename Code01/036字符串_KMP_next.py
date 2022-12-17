# 输入一个列表生成对应的next列表


# 暴力法
def getNext1(st):
    if len(st) <= 1:
        return None
    next = [None for i in range(len(st))]   # 初始化一个长度和原列表相同的列表

    next[0] = -1
    next[1] = 0
    for i in range(2, len(st)):
        x = 0
        j = i - 1
        max = 0
        tLen = 0

        while tLen < i-1: # 前后缀的长度不能大于等于当前字符
            if st[0:tLen+1] == st[i-tLen-1:i] and max < len(st[i-tLen-1:i]):
                max = len(st[i-tLen-1:i])
            tLen += 1
        next[i] = max
    return next



def getNext(st):
    if len(st) <= 1:
        return None
    next = [None for i in range(len(st))]   # 初始化一个长度和原列表相同的列表
    next[0] = -1
    next[1] = 0
    
    for i in range(2, len(st)):
        t = next[i - 1] 
        while t != -1:
            if st[t] == st[i - 1]:
                next[i] = t + 1 # 重点！！！！
                break
            else:
                t = next[t]
        if t == -1:
            next[i] = 0
    return next

import random
# 两种做法的对数器
times = 100
for i in range(times):
    st = ""
    for j in range(2,300):# 长度
        t = chr(64 + random.randint(0,25))
        l1 = getNext1(t)
        l2 = getNext(t)
    if l1 != l2:
        break
if i == times - 1:
    print("NICE!!!!")
else:
    print("CUCKED!!!!!")
