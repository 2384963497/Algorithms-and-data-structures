stones = [4,3,4,3,2]

def heapify(l): # 大根堆
    deep = len(l) - 1
    for i in range(deep + 1):
        j = i
        while j > 0 and l[j] > l[(j - 1) // 2]:
            l[j], l[(j - 1) // 2] = l[(j - 1) // 2], l[j]
            j = (j - 1) // 2
    return l

def heapinsert(l):
    deep = len(l) - 1
    i = 0
    while i * 2 + 1 <= deep:
        temp = i * 2 + 1
        if i * 2 + 2 <= deep and l[i * 2 + 2] > l[temp]:
            temp = i * 2 + 2
        if l[i] < l[temp]:
            l[i], l[temp] = l[temp], l[i]
            i = temp
        else:
            break
    

heapify(stones)
while len(stones) > 1:
    t = stones.pop(0)
    heapify(stones)
    stones[0] = t - stones[0]
    if stones[0] == 0:
        stones.pop(0)
        heapify(stones)
    else:
        heapinsert(stones)
    

# if len(stones) == 1:
#     return stones[0]
# else:
#     return 0





