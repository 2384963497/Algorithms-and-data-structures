# 题目描述
# 设有 n 个正整数 a1…an，将它们联接成一排，相邻数字首尾相接，组成一个最大的整数。
# 输入格式
# 第一行有一个整数，表示数字个数 n。
# 第二行有 n 个整数，表示给出的 n 个整数 ai。
# 输出格式
# 一个正整数，表示最大的整数
# 输入输出样例
# 输入 #1复制
# 3
# 13 312 343
# 输出 #1复制
# 34331213
# 输入 #2复制
# 4
# 7 13 4 246
# 输出 #2复制
# 7424613

def myCmp(a, b):
    if a+b > b+a:
        return 1
    return 0

def mySort(nList):
    lLen = len(nList)

    for i in range(lLen):#heapInsert生成小根堆
        j = i 
        while j > 0:
            if myCmp(nList[j], nList[(j-1)//2]):
                break
            nList[j], nList[(j-1)//2] = nList[(j-1)//2], nList[j]
            j = (j-1)//2
    
    #heapify
    lLen -= 1
    while lLen > 0:
        nList[0], nList[lLen] = nList[lLen], nList[0]
        lLen -= 1

        i = 0
        j = 2*i+1
        while j <= lLen:
            temp = j
            if j+1 <= lLen and not myCmp(nList[j+1], nList[j]):
                temp = j+1
            if not myCmp(nList[i], nList[temp]):
                temp = i
            if i == temp:
                break
            nList[i], nList[temp] = nList[temp], nList[i]
            i = temp
            j = i*2+1
    return nList

n = int(input(""))
nList = [None for i in range(n)]
nList = input("").split(' ')

nList = mySort(nList)

s=''
for i in nList:
    s+=i
print(s)