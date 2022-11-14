from collections import deque

# 比较器
def cmp(a, b):
    if a.data < b.data:
        return -1
    elif a.data > b.data:
        return 1
    return 0

# 快速排序
def quickSort(tList):
    nLen = len(tList)

    if nLen <= 1:
        return tList

    mid = tList[0]
    smaller = -1 
    bigger = nLen

    i = 1
    while i < bigger:
        if cmp(tList[i], tList[smaller+1]) == -1:
            tList[i], tList[smaller+1] = tList[smaller+1], tList[i]
            smaller += 1
        elif cmp(tList[i], tList[bigger-1]) == 1:
            tList[i], tList[bigger-1] = tList[bigger-1], tList[i]
            bigger -= 1
            i -= 1
        i += 1
    if smaller == -1:
        sList = []
    else:
        sList = quickSort(tList[:smaller+1])
    if bigger == nLen:
        bList = []
    else:
        bList = quickSort(tList[bigger:])

    return sList + tList[smaller+1:bigger] + bList

# 节点类
class Node():
    def __init__(self, data):
        self.data = data
        self.lNode = None
        self.rNode = None
        self.paNode = None  # 父节点

# 构建树
class hTree():

    def __init__(self, chList):
       # 生成哈夫曼树
       # 1.将列表中的值都转为节点类
        nodeList = list()
        for i in chList:
            tempNode = Node(i)
            nodeList.append(tempNode)
        
        while len(nodeList) > 1:
            # 排序-----比较器
            nodeList = quickSort(nodeList)
            # 组合两个子树
            lTree =  nodeList.pop(0)
            rTree =  nodeList.pop(0)
            fTree = Node(rTree.data + lTree.data)
            fTree.lNode = lTree
            fTree.rNode = rTree
            rTree.paNode = fTree
            lTree.paNode = fTree
            # 将新树加入    
            nodeList.append(fTree)
        # 
        self.root = nodeList[0]
        nodeList.pop()

    # 对字符进行编码
    def find(self, key):
        tempQueue = deque()
        tempQueue.append(self.root)
        
        while True:
            tempNode = tempQueue.popleft()
            if tempNode.lNode == None and tempNode.rNode == None and tempNode.data == key:
                keyNode =  tempNode
                break
            if tempNode.lNode != None:
                tempQueue.append(tempNode.lNode)
            if tempNode.rNode != None:
                tempQueue.append(tempNode.rNode)
        # 找到指定字符的位置
        # 回溯出路径
        result = ''
        while keyNode.paNode != None:
            if keyNode.paNode.lNode == keyNode:
                result += '0'
                keyNode = keyNode.paNode
                continue
            if keyNode.paNode.rNode == keyNode:
                result += '1'
                keyNode = keyNode.paNode

        result = result[::-1]
        return result        
        
    # 解码
    def decode(self, inStr):
        outStr = ''
        tempNode = self.root
        for i in inStr:
            if tempNode.lNode == None and tempNode.rNode == None:
                for j in chDict:
                    if chDict[j][0] == tempNode.data:
                        outStr += j
                        tempNode = self.root
            if i == '0':
                tempNode = tempNode.lNode
            else:
                tempNode = tempNode.rNode
        return outStr

if __name__ == '__main__':
    # 1.打卡文件 并统计词频字典
    chDict = dict()
    with open(r"F:\\Course.txt", 'r') as rstream:
        tempStr = rstream.read()
    
    for i in tempStr:
        if i not in chDict:
            chDict[i] = 1
        else:
            chDict[i] += 1
    # 测试输出
    # for i in chDict:
    #     print(f"{i} :  {chDict[i]}")
    
    # 2.生成哈夫曼树
    myTree = hTree(chDict.values())

    # 3.根据哈夫曼树更新字典
    for i in chDict:
        temp = myTree.find(chDict[i])
        chDict[i] = [chDict[i], temp]
        # print(i,':',chDict[i])
    
    # 4.创建压缩
    with open("F:\\Huff.txt", 'w') as wstream:
        for i in tempStr:
            temp = chDict[i][1]
            wstream.write(temp)
    # 5.ascii码源文件
    with open("F:\\Ascii.txt", 'w') as wstream:
        for i in tempStr:
            temp = str(bin(ord(i)))[2:]
            wstream.write(temp)
    
    # 6.哈夫曼解码
    with open("F:\\Huff.txt", 'r') as rstream:
        temp = rstream.read()
        temp = myTree.decode(temp)
        with open("F:\\Huff_decode.txt", 'w') as wstream:
            wstream.write(temp)
    

    # 7.统计哈夫曼编码和Ascii码编码的长度
    with open("F:\\Huff.txt", 'r') as rstream:
        temp = rstream.read()
        count = 0
        for i in temp:
            count += 1 
    print(f"哈夫曼编码后二进制个数为: {count:,}")
    with open("F:\\Ascii.txt", 'r') as rstream:
        temp = rstream.read()
        count = 0
        for i in temp:
            count += 1 
    print(f"Ascii码二进制个数为:\t  {count:,}")