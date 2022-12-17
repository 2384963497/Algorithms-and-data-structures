
def heapSort(nli):

    for i in range(len(nli)):
        j = i 
        while j > 0:
            # if nli[j] > nli[(j-1)//2]:  #升序的大根堆
            if nli[j] < nli[(j-1)//2]:  #降序的小根堆
                nli[j], nli[(j-1)//2] = nli[(j-1)//2], nli[j]
                j =  (j-1)//2
            else:
                break
    #使整个堆变成大根堆

    #开始排序
    lLen = len(nli)-1
    while lLen > 0:
        nli[0], nli[lLen] = nli[lLen], nli[0]
        lLen-=1

        i = 0
        j = 2*i+1
        while j <= lLen:
            temp = j
            # if j+1 <= lLen and nli[j] < nli[j+1]:   #子节点的较大值
            if j+1 <= lLen and nli[j] > nli[j+1]:   #子节点的较小值
                temp = j+1
            if nli[i] < nli[temp]:
                temp = i
            
            if i == temp:
                break
            else:
                nli[i], nli[temp] = nli[temp], nli[i] 
                i = temp
                j = 2*i+1

    return nli



import random
times=1000
lLen=100
for i in range(times):
    nList=[]
    for j in range(lLen):
        temp = random.randint(-100,100)
        nList.append(temp)
    r1 = sorted(nList, reverse=True)
    r2 = heapSort(nList)

    if r1 != r2:
        break

if i == times-1:
    print("NICE!!!!")
else:
    print("Fucking Fucked!")
