# rt

from collections import deque

# 定义节点类
class Node():
    def __init__(self, data):
        self.data = data
        self.lnode = None
        self.rnode = None

class bTree():
    def __init__(self):
        self.root = None
        self.size = 0
    
    def isEmpty(self):
        if self.size == 0:
            return True
        return False
    
    def numNodes(self):
        return self.size
    
    def add(self, data):
        tempNode = Node(data)
        if self.size == 0:
            self.root = tempNode
            self.size += 1 
            return 
        tempQueue = deque()
        tempQueue.append(self.root)
        while True:
            temp = tempQueue.popleft()
            if temp.lnode == None:
                temp.lnode = tempNode
                self.size += 1
                break
            elif temp.rnode == None:
                temp.rnode = tempNode
                self.size += 1
                break
            else:
                tempQueue.append(temp.lnode)
                tempQueue.append(temp.rnode)
    
    # 层次遍历
    def travel(self):
        if self.size == 0:
            return None
        tempQueue = deque()
        tempQueue.append(self.root)
        while tempQueue.__len__() > 0:
            temp = tempQueue.popleft()
            print(temp.data, end = ' ')
            if temp.lnode != None:
                tempQueue.append(temp.lnode)
            if temp.rnode != None:
                tempQueue.append(temp.rnode)


if __name__ == '__main__':
    mybTree = bTree()
    mybTree.add(1)
    mybTree.add(2)
    mybTree.add(3)
    mybTree.add(4)
    mybTree.add(5)
    mybTree.add(6)
    mybTree.add(7)
    mybTree.add(8)
    mybTree.add(9)

    print(mybTree.size)
    mybTree.travel()




