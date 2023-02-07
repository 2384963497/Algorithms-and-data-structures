def quickSort(li):
    if len(li) == 1:
        return li

    samll = -1
    big = len(li)
    key = li[(len(li) - 1) // 2] 
    mid = 0

    i = 0
    while i < big:
        if li[i] < key:
            li[i], li[samll + 1] = li[samll + 1], li[i]
            samll += 1
        elif li[i] > key:
            li[i], li[big - 1] = li[big - 1], li[i]
            big -= 1
            i -= 1
        else:
            mid += 1
        i += 1
    
    if samll == -1:
        sLi = []
    else:
        sLi = quickSort(li[:samll + 1])

    if big == len(li):
        bLi = []
    else:
        bLi = quickSort(li[big:])

    return sLi + [key] * mid + bLi


import random
times=100
lLen=100
for i in range(times):
    nList=[]
    for j in range(lLen):
        temp = random.randint(-100,100)
        nList.append(temp)
    r2 = quickSort(nList)
    r1 = sorted(nList)

    if r1 != r2:
        break

if i == times-1:
    print("NICE!!!!")
else:
    print("Fucking Fucked!")