def bucketSort(nli):
    temp = max(nli)
    k = 0
    while temp:
        temp /= 10
        k += 1
    
    q=1
    while k > 0:
        bucket=[list() for i in range(10)]  #生成桶
        for j in nli:
            bucket[int(j%(q*10)/q)].append(j)  #每一轮装入桶
        q *= 10

        temp = 0
        for i in bucket:
            for j in i:
                nli[temp] = j
                temp += 1
        k-=1

    return nli



import random
times=100
lLen=100
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
