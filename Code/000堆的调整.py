import random

def heapSort(nli):
    deep = len(nli)-1

    while deep >= 0:
        nli[0], nli[deep] = nli[deep], nli[0]
        deep-=1

        i = 0
        j = 2*i+1
        while j <= deep:
            temp = j 
            if j+1 <= deep and nli[j] < nli[j+1]:
                temp = j+1
            if nli[temp] < nli[i]:
                temp = i  #temp保存的是局部父子间最大值的下标
            if temp == i:
                break
            nli[i], nli[temp] = nli[temp], nli[i]
            i = temp
            j = i*2+1

    return nli

def heapInsert(nli):
    lLen = len(nli)
    for i in range(lLen):
        j = i
        while nli[j] > nli[(j-1)//2] and j > 0:
            nli[j], nli[(j-1)//2] = nli[(j-1)//2], nli[j]
            j = (j-1)//2
    return nli

li=[]
for i in range(20):
    temp=random.randint(1,200)
    li.append(temp)

print(li)
li = heapInsert(li)
print(li)
li = heapSort(li)
print(li)

