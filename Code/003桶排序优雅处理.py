def bucketSort(nli):
    temp = max(nli)
    k = 0
    while temp:
        temp /= 10
        k += 1
    
    lLen = len(nli)
    q=1
    while k > 0:
        tli = [0 for i in range(10)]

        for i in nli:   #统计当前位的词频
            index=int(i % (q*10) / q)
            tli[index] += 1

        for i in range(1,10):   #将词频数组中的每一位都计算出前缀和
            tli[i] += tli[i-1]

        cli=[0 for i in range(lLen)]    #准备一个和元素组长度相等的数组,初始化为0
        i = lLen-1
        while i >= 0:
            index = tli[int(nli[i] % (q*10) / q)]-1
            cli[index] = nli[i]
            tli[int(nli[i] % (q*10) / q)] -= 1
            i-=1
        nli = cli
        q *= 10
        k-=1
        

    return nli



import random
times=100
lLen=10
for i in range(times):
    nList=[]
    for j in range(lLen):
        temp = random.randint(0,1000)
        nList.append(temp)
    r1 = sorted(nList)
    r2 = bucketSort(nList)

    if r1 != r2:
        break

if i == times-1:
    print("NICE!!!!")
else:
    print("Fucking Fucked!")
