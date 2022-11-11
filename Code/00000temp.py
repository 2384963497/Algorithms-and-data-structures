
# class Node():
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# def func(tlist):
#     tlist[2], tlist[3] = tlist[3], tlist[2]


# l = [Node(20), Node(1), Node(2), Node(23), Node(250)]

# for i in l:
#     print(i.data, end = ' ')
# func(l)
# print("\n--------------------")
# for i in l:
#     print(i.data, end = ' ')


# # 比较器
# def cmp(a, b):
#     if a.data < b.data:
#         return -1
#     elif a.data > b.data:
#         return 1
#     return 0

# # 快速排序
# def quickSort(tList):
#     nLen = len(tList)

#     if nLen <= 1:
#         return tList

#     mid = tList[0]
#     smaller = -1 
#     bigger = nLen

#     i = 1
#     while i < bigger:
#         if cmp(tList[i], tList[smaller+1]) == -1:
#             tList[i], tList[smaller+1] = tList[smaller+1], tList[i]
#             smaller += 1
#         elif cmp(tList[i], tList[bigger-1]) == 1:
#             tList[i], tList[bigger-1] = tList[bigger-1], tList[i]
#             bigger -= 1
#             i -= 1
#         i += 1
#     if smaller == -1:
#         sList = []
#     else:
#         sList = quickSort(tList[:smaller+1])
#     if bigger == nLen:
#         bList = []
#     else:
#         bList = quickSort(tList[bigger:])

#     return sList + tList[smaller+1:bigger] + bList

# # 节点类
# class Node():
#     def __init__(self, data):
#         self.data = data
#         self.lNode = None
#         self.rNode = None
#         self.paNode = None  # 父节点

# # 构建树
# class hTree():
#     def __init__(self, chList):


#        # 生成哈夫曼树
#        # 1.将列表中的值都转为节点类
#         nodeList = list()
#         for i in chList:
#             tempNode = Node(i)
#             nodeList.append(tempNode)
        
#         while len(nodeList) > 1:
#             # 排序-----比较器
#             nodeList = quickSort(nodeList)
#             # 组合两个子树
#             lTree =  nodeList.pop(0)
#             rTree =  nodeList.pop(0)
#             fTree = Node(rTree.data + lTree.data)
#             fTree.lNode = lTree
#             fTree.rNode = rTree
#             rTree.paNode = fTree
#             lTree.paNode = fTree
#             # 将新树加入    
#             nodeList.append(fTree)
#         # 
#         self.root = nodeList[0]
#         nodeList.pop()






# if __name__ == '__main__':
#     # 1. 打卡文件 并统计词频字典
#     chDict = dict()
    
#     chDict = {'a':100, 'b':20, 'e':250, '5':12, 's':10}


#     # 测试输出
#     # for i in chDict:
#     #     print(f"{i} :  {chDict[i]}")
    
#     # 生成哈夫曼树
#     myTree = hTree(chDict.values())
#     a = 1


# rt

# from collections import deque

# # 定义节点类
# class Node():
#     def __init__(self, data):
#         self.data = data
#         self.lnode = None
#         self.rnode = None

# class bTree():
#     def __init__(self):
#         self.root = None
#         self.size = 0
    
#     def isEmpty(self):
#         if self.size == 0:
#             return True
#         return False
    
#     def numNodes(self):
#         return self.size
    
#     def add(self, data):
#         tempNode = Node(data)
#         if self.size == 0:
#             self.root = tempNode
#             self.size += 1 
#             return 
#         tempQueue = deque()
#         tempQueue.append(self.root)
#         while True:
#             temp = tempQueue.popleft()
#             if temp.lnode == None:
#                 temp.lnode = tempNode
#                 self.size += 1
#                 break
#             elif temp.rnode == None:
#                 temp.rnode = tempNode
#                 self.size += 1
#                 break
#             else:
#                 tempQueue.append(temp.lnode)
#                 tempQueue.append(temp.rnode)
    
#     # 查找指定值的叶子节点并返回
#     def findFunc(self, key): 
#         tempQueue = deque()
#         tempQueue.append(self.root)
        
#         while True:
#             tempNode = tempQueue.popleft()
#             if tempNode.lnode != None:
#                 tempQueue.append(tempNode.lnode)
#             if tempNode.rnode != None:
#                 tempQueue.append(tempNode.rnode)
#             if tempNode.lnode == None and tempNode.rnode == None and tempNode.data == key:
#                 return tempNode
#                 break

    

# if __name__ == '__main__':
#     mybTree = bTree()

#     mybTree.add(0)
#     mybTree.add(1)
#     mybTree.add(2)
#     mybTree.add(3)
#     mybTree.add(4)
#     mybTree.add(5)
#     mybTree.add(6)
#     mybTree.add(7)
#     mybTree.add(8)
#     mybTree.add(9)


#     rNode = mybTree.findFunc(9)
#     print(rNode.data)



import random
l1 = [chr(i+97) for i in range(26)]
l2 = [chr(i+65) for i in range(26)]
l2.append('\n')
# print(l1)
# print(l2)
with open(r"F:\\Course.txt", 'w') as wstream:
    for i in range(100000):
        j = random.randint(0,10)
        if j <= 2:
            temp = random.choice(l2)
        else:
            temp = random.choice(l1)
        wstream.write(temp)